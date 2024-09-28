from django.contrib import admin


class HabitAdmin(admin.ModelAdmin):
    """
    Админка модели Habit
    """
    list_display = ("id", "habit", "sign_of_a_pleasant_habit", "related_habit", "reward")
    list_filter = ("sign_of_a_pleasant_habit", )
    search_fields = ("habit", )
