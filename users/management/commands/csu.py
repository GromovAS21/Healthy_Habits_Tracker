from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания superuser`а
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@test.ru",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password("Qwerty")
        user.save()
