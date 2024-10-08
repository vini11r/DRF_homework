# Generated by Django 5.0.7 on 2024-07-30 20:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0002_alter_user_options_remove_user_username_user_avatar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_payment",
                    models.DateField(auto_now_add=True, verbose_name="Дата оплаты"),
                ),
                (
                    "payment_sum",
                    models.PositiveIntegerField(verbose_name="Сумма оплаты"),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("cash", "Наличные"), ("transfer", "Перевод на счет")],
                        max_length=20,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paid_courses",
                        to="materials.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paid_lesson",
                        to="materials.course",
                        verbose_name="Оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата",
                "verbose_name_plural": "Оплаты",
            },
        ),
    ]
