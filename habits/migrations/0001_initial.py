import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("habit", models.CharField(max_length=255, verbose_name="Привычка")),
                (
                    "place_of_execution",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Место где нужно выполнять привычку",
                    ),
                ),
                (
                    "time_execution",
                    models.TimeField(
                        blank=True,
                        null=True,
                        verbose_name="Время когда выполняется привычка",
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveSmallIntegerField(
                        default=1, verbose_name="Периодичность привычки"
                    ),
                ),
                (
                    "time_to_complete",
                    models.DurationField(
                        default=datetime.timedelta(seconds=120),
                        verbose_name="Продолжительность выполнения привычки по времени",
                    ),
                ),
                (
                    "sign_of_a_pleasant_habit",
                    models.BooleanField(
                        default=False, verbose_name="Показатель приятной привычки"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True, null=True, verbose_name="Вознаграждение за привычку"
                    ),
                ),
                (
                    "published",
                    models.CharField(
                        choices=[
                            ("Опубликован", "Опубликован"),
                            ("Не опубликован", "Не опубликован"),
                        ],
                        default="Не опубликован",
                        max_length=50,
                        verbose_name="Статус опубликования привычки",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="useful_habits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель привычки",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="related_habits",
                        to="habits.habit",
                        verbose_name="Связанная приятная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ("id",),
            },
        ),
    ]
