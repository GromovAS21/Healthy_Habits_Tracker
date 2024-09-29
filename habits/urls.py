from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitsViewSet, UserHabitViewSet

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"habits", HabitsViewSet, basename="habits")

urlpatterns = [
    path("user-habits-list/", UserHabitViewSet.as_view(), name="user_habits_list")
] + router.urls
