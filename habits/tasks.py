from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit_notice():
    """Отправляет уведомление о необходимости выполнить действие по привычке"""
    zone = pytz.timezone(settings.TIME_ZONE)
    time_now = datetime.now(zone)
    start_time = time_now - timedelta(minutes=10)
    finish_time = time_now + timedelta(minutes=10)

    habits = Habit.objects.filter(time__gte=start_time, time__lte=finish_time)

    for habit in habits:
        owner = habit.owner
        action = habit.action
        place = habit.place
        time = habit.time
        duration = habit.duration
        chat_id = owner.id_telegram

        if chat_id:
            message = (
                f"У вас есть привычка в/на {place}:"
                f"\n{action}\n"
                f"Время: {time}\n"
                f"Продолжительность: {duration} секунд"
            )
            send_telegram_message(message, chat_id)
            habit.time = habit.time + timedelta(days=habit.periodicity)
            habit.save()
