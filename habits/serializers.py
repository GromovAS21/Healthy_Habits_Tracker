from rest_framework import serializers

from habits.models import Habit
from habits.validators import FieldFillingValidator, ExecutionTimeValidator


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit
    """

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            FieldFillingValidator("reward", "related_habit"),
            ExecutionTimeValidator("time_to_complete")
        ]
