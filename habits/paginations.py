from rest_framework.pagination import PageNumberPagination


class ViewUserHabitPagination(PageNumberPagination):
    """
    Пагинация при выводе списка привычек пользователя
    """
    page_size = 5