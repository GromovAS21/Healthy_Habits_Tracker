from datetime import timedelta

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from habits.models import Habit
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


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

    def get_permissions(self):
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsOwner | IsAdminUser]
        return super().get_permissions()




