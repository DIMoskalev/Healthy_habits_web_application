from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь, создавший привычку",
        **NULLABLE,
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        help_text="Укажите место, где выполняется привычка",
    )
    time = models.DateTimeField(
        verbose_name="Дата и время выполнения привычки",
        help_text="Укажите дату и время выполнения привычки",
        auto_now_add=True,
    )
    action = models.CharField(
        max_length=100,
        verbose_name="Действие привычки",
        help_text="Укажите действие, которое нужно выполнять",
    )
    is_pleasant_habit = models.BooleanField(
        verbose_name="Является ли привычка приятной",
        help_text="Укажите, является ли привычка приятной",
        default=True,
    )
    related_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    periodicity = models.PositiveIntegerField(
        verbose_name="Периодичность выполнения привычки",
        help_text="Укажите периодичность выполнения привычки в днях",
        default=1,
        **NULLABLE,
    )
    reward = models.CharField(
        max_length=100,
        verbose_name="Награда за привычку",
        help_text="Укажите награду за привычку",
        **NULLABLE,
    )
    duration = models.DurationField(
        verbose_name="Продолжительность выполнения привычки по времени в секундах",
        help_text="Укажите продолжительность выполнения привычки в секундах",
        **NULLABLE,
    )
    is_public = models.BooleanField(
        verbose_name="Публичная привычки",
        help_text="Укажите, является ли привычка публичной",
        default=True,
    )

    def __str__(self):
        return f"{self.owner} - {self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
