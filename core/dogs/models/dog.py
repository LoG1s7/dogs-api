from django.db import models
from django.utils.translation import gettext_lazy as _


class Dog(models.Model):
    """Модель собаки."""

    class Gender(models.TextChoices):
        """Enum модель для выбора пола собаки."""

        MALE = "male", _("Male")
        FEMALE = "femail", _("Femail")

    name = models.CharField("Имя", max_length=100)
    age = models.IntegerField("Возраст")
    breed = models.ForeignKey(
        "Breed",
        verbose_name="Порода",
        on_delete=models.CASCADE,
        related_name="dogs",
    )
    gender = models.CharField(
        verbose_name="Пол",
        choices=Gender.choices,
        max_length=100,
    )
    color = models.CharField(verbose_name="Цвет", max_length=100)
    favorite_food = models.CharField(
        verbose_name="Любимая еда",
        max_length=100,
    )
    favorite_toy = models.CharField(
        verbose_name="Любимая игрушка",
        max_length=100,
    )

    class Meta:
        """Имена модели в единственном и множественном числе на русском."""

        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self) -> str:
        return f"{self.name}"
