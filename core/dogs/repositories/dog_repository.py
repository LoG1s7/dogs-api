from typing import Any

from django.shortcuts import get_object_or_404

from dogs.models.dog import Dog
from dogs.repositories.base_repository import BaseRepositoryInterface


class DogRepository(BaseRepositoryInterface):
    """Репозиторий для управления объектами Dog.
    Реализует интерфейс BaseRepositoryInterface.
    """

    def list(self) -> list[Dog]:
        """Возвращает список всех объектов Dog."""
        return Dog.objects.all()

    def get(self, pk: int) -> Dog:
        """Получает объект Dog по его первичному ключу."""
        return get_object_or_404(Dog, pk=pk)

    @classmethod
    def create(cls, data: dict[str, Any]) -> Dog:
        """Создает новый объект Dog с указанными данными."""
        return Dog.objects.create(
            name=data["name"],
            breed_id=data["breed_id"],
            age=data["age"],
            gender=data["gender"],
            color=data["color"],
            favorite_food=data["favorite_food"],
            favorite_toy=data["favorite_toy"],
        )

    def update(self, pk: int, data: dict[str, Any]) -> Dog:
        """Обновляет существующий объект Dog с указанными данными."""
        dog = self.get(pk)
        for key, value in data.items():
            setattr(dog, key, value)
        dog.save()
        return dog

    def delete(self, pk: int) -> None:
        """Удаляет объект Dog по его первичному ключу."""
        dog = self.get(pk)
        dog.delete()
