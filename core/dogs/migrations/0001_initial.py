# Generated by Django 5.1.1 on 2024-10-03 08:08

import django.core.validators
import django.db.models.deletion
import dogs.utils.custom_types
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Breed",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название породы"),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("tiny", "Tiny"),
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("large", "Large"),
                        ],
                        max_length=10,
                        verbose_name="Размер",
                    ),
                ),
                (
                    "friendliness",
                    dogs.utils.custom_types.CustomIntegerField(
                        db_column="friendliness",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Дружелюбность",
                    ),
                ),
                (
                    "trainability",
                    dogs.utils.custom_types.CustomIntegerField(
                        db_column="trainability",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Обучаемость",
                    ),
                ),
                (
                    "shedding_amount",
                    dogs.utils.custom_types.CustomIntegerField(
                        db_column="shedding_amount",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Линька",
                    ),
                ),
                (
                    "exercise_needs",
                    dogs.utils.custom_types.CustomIntegerField(
                        db_column="exercise_needs",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Потребность в упражнениях",
                    ),
                ),
            ],
            options={
                "verbose_name": "Порода",
                "verbose_name_plural": "Породы",
            },
        ),
        migrations.CreateModel(
            name="Dog",
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
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("age", models.IntegerField(verbose_name="Возраст")),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("femail", "Femail")],
                        max_length=100,
                        verbose_name="Пол",
                    ),
                ),
                ("color", models.CharField(max_length=100, verbose_name="Цвет")),
                (
                    "favorite_food",
                    models.CharField(max_length=100, verbose_name="Любимая еда"),
                ),
                (
                    "favorite_toy",
                    models.CharField(max_length=100, verbose_name="Любимая игрушка"),
                ),
                (
                    "breed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dogs",
                        to="dogs.breed",
                        verbose_name="Порода",
                    ),
                ),
            ],
            options={
                "verbose_name": "Собака",
                "verbose_name_plural": "Собаки",
            },
        ),
    ]
