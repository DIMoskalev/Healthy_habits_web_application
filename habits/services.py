import requests
from django.conf import settings
from rest_framework import status


def send_telegram_message(message, chat_id):
    """ Функция отправляет сообщение через Telegram-бота """
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    response = requests.get(f'{settings.TELEGRAM_URL}{settings.TOKEN_BOT}/sendMessage', params=params)
    if response.status_code != status.HTTP_200_OK:
        raise ValueError(f'Ошибка отправки сообщения Telegram: {response.text}')
