from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Заполните описание курса"
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        blank=True,
        null=True,
        help_text="Загрузите картинку",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Заполните описание урока"
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        blank=True,
        null=True,
        help_text="Загрузите картинку",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="lessons",
        verbose_name="Курс",
        blank=True,
        null=True,
        help_text="Укажите курс",
    )
    video = models.URLField(
        max_length=400, blank=True, null=True, help_text="Укажите ссылку на видео"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
