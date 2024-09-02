from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def check_user():
    """
    Отправляет письмо с уведомлением о блокировке аккаунта.
    """
    users = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=30), is_active=True)
    email_list = []
    for user in users:
        user.is_active = False
        user.save()
        email_list.append(user.email)
    if email_list:
        send_mail(
            subject="ВНИМАНИЕ!",
            message="Ваш аккаунт заблокирован",
            from_email=EMAIL_HOST_USER,
            recipient_list=email_list,
        )

