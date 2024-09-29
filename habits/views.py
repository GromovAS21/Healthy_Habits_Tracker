from datetime import timedelta

from rest_framework import viewsets

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Habit
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """
        Добавление владельца к Habit при создании
        """
        serializer.save(owner=self.request.user)



