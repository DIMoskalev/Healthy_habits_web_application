from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (ChoiceValidator, PeriodicityValidator,
                               PleasantRelatedValidator, PleasantValidator,
                               TimeValidator)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            ChoiceValidator(field1="related_habit", field2="reward"),
            TimeValidator(field="duration"),
            PleasantRelatedValidator(
                field1="related_habit", field2="is_pleasant_habit"
            ),
            PleasantValidator(
                field1="is_pleasant_habit", field2="reward", field3="related_habit"
            ),
            PeriodicityValidator(field="periodicity"),
        ]
