from datetime import timedelta

from rest_framework.validators import ValidationError


class FieldFillingValidator:
    """
    Валидатор для проверки одновременного заполнения полей reward и related_habit
    """
    def __init__(self, reward, related_habit):
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        reward_field = value.get(self.reward)
        related_habit_field = value.get(self.related_habit)

        if reward_field and related_habit_field:
            raise ValidationError("Может быть заполнено поле reward или поле related_habit")


class ExecutionTimeValidator:
    """
    Валидатор для проверки продолжительности выполнения привычки не более 120 секунд
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = value.get(self.field)
        if time_to_complete:
            if time_to_complete > timedelta(seconds=120):
                raise ValidationError("Продолжительность выполнения привычки не может быть более 120 секунд")


class RelatedHabitValidator:
    """
    Валидатор для проверки связанной привычки на принадлежность к приятной привычки
    """

    def __init__(self, related_habit):
        self.related_habit = related_habit

    def __call__(self, value):
        habit = value.get(self.related_habit)
        if habit:
            if not habit.sign_of_a_pleasant_habit:
                raise ValidationError("Связанная привычка должна быть приятной")










