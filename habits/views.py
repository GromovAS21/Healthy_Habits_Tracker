
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from habits.models import Habit
from habits.paginations import ViewUserHabitPagination
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


class UserHabitViewSet(APIView):
    """
    Представление для получения списка всех привычек пользователя
    """

    # pagination_class = ViewUserHabitPagination

    def get(self, request):
        habits = Habit.objects.filter(owner=request.user)
        paginator = ViewUserHabitPagination()
        result = paginator.paginate_queryset(habits, request)
        serializer = HabitSerializer(result, many=True)
        return Response(serializer.data)


