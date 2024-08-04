from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=150,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=150,
        verbose_name="Город",
        help_text="Укажите город",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_METHOD = (
        ("cash", "Наличные"),
        ("transfer", "Перевод на счет"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payments", verbose_name="Пользователь"
    )
    date_payment = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="paid_courses",
                                    verbose_name="Оплаченный курс", blank=True, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="paid_lesson",
                                    verbose_name="Оплаченный урок", blank=True, null=True)
    payment_sum = models.PositiveIntegerField(verbose_name="Сумма оплаты", blank=True, null=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"{self.user} - {self.paid_course if self.paid_course else self.paid_lesson}"
