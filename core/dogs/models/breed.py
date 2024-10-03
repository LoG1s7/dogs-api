from django.db import models
from django.utils.translation import gettext_lazy as _

from dogs.utils.custom_types import CustomIntegerField


class Breed(models.Model):
    """Модель породы собаки."""

    class Sizes(models.TextChoices):
        TINY = "tiny", _("Tiny")
        SMALL = "small", _("Small")
        MEDIUM = "medium", _("Medium")
        LARGE = "large", _("Large")

    name = models.CharField(
        verbose_name="Название породы",
        max_length=100,
        unique=True,
    )
    size = models.CharField(
        verbose_name="Размер",
        choices=Sizes.choices,
        max_length=10,
    )
    friendliness = CustomIntegerField(
        verbose_name="Дружелюбность", db_column="friendliness"
    )
    trainability = CustomIntegerField(
        verbose_name="Обучаемость", db_column="trainability"
    )
    shedding_amount = CustomIntegerField(
        verbose_name="Линька", db_column="shedding_amount"
    )
    exercise_needs = CustomIntegerField(
        verbose_name="Потребность в упражнениях", db_column="exercise_needs"
    )

    class Meta:
        """Имена модели в единственном и множественном числе на русском."""

        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self) -> str:
        return f"{self.name}"
