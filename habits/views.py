from django.shortcuts import render
from rest_framework import viewsets

from habits.models import Habit
from habits.serializers import HabitsSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Habit
    """

    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """
        Добавление владельца к хабиту при создании
        """
        serializer.save(owner=self.request.user)



