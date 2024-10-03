from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CustomIntegerField(models.IntegerField):
    description = "Целочисленное поле с ограничением значений от 1 до 5"

    def __init__(self, *args, **kwargs) -> None:
        kwargs["validators"] = [
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
        super().__init__(*args, **kwargs)
