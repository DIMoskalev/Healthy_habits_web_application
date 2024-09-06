from datetime import timedelta

from rest_framework.serializers import ValidationError


class ChoiceValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if value.get('related_habit') and value.get('reward'):
            message = 'Нельзя одновременно заполнять поле вознаграждения и поле связанной привычки'
            raise ValidationError(message)


class TimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('duration') and value.get('duration') > timedelta(seconds=120):
            message = 'Время выполнения должно быть не больше 120 секунд'
            raise ValidationError(message)


class PleasantRelatedValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        if value.get('related_habit'):
            if value.get('is_pleasant_habit') is False:
                message = 'В связанные привычки могут попадать только привычки с признаком приятной привычки'
                raise ValidationError(message)


class PleasantValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        if value.get('is_pleasant_habit'):
            if value.get('reward') or value.get('related_habit'):
                message = 'У приятной привычки не может быть вознаграждения или связанной привычки'
                raise ValidationError(message)


class PeriodicityValidator:
    def __init__(self, field):
        self.field1 = field

    def __call__(self, value):
        if value.get('periodicity'):
            if value.get('periodicity') < 1 or value.get('periodicity') > 7:
                message = 'Нельзя выполнять привычку реже, чем 1 раз в 7 дней'
                raise ValidationError(message)
