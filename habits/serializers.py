from rest_framework import serializers

from habits.models import Habit
from habits.validators import FieldFillingValidator, frequency_of_habit_validator, \
    RelatedHabitValidator, execution_time_validator


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit
    """

    time_to_complete = serializers.DurationField(validators=[execution_time_validator], required=False)
    periodicity = serializers.IntegerField(validators=[frequency_of_habit_validator], required=False)

    class Meta:
        model = Habit
        exclude = ("send_indicator",)
        validators = [
            FieldFillingValidator("reward", "related_habit", "sign_of_a_pleasant_habit"),
            RelatedHabitValidator("related_habit")
        ]


