from typing import Any

from django.shortcuts import get_object_or_404

from dogs.models.breed import Breed
from dogs.repositories.base_repository import BaseRepositoryInterface


class BreedRepository(BaseRepositoryInterface):
    """Репозиторий для управления объектами Breed.
    Реализует интерфейс BaseRepositoryInterface.
    """

    def list(self) -> list[Breed]:
        """Возвращает список всех объектов Breed."""
        return Breed.objects.all()

    def get(self, pk: int) -> Breed:
        """Получает объект Breed по его первичному ключу."""
        return get_object_or_404(Breed, pk=pk)

    def create(self, data: dict[str, Any]) -> Breed:
        """Создает новый объект Breed с указанными данными."""
        return Breed.objects.create(
            name=data["name"],
            size=data["size"],
            friendliness=data["friendliness"],
            trainability=data["trainability"],
            shedding_amount=data["shedding_amount"],
            exercise_needs=data["exercise_needs"],
        )

    def update(self, pk: int, data: dict[str, Any]) -> Breed:
        """Обновляет существующий объект Breed с указанными данными."""
        breed = self.get(pk)
        for key, value in data.items():
            setattr(breed, key, value)
        breed.save()
        return breed

    def delete(self, pk: int) -> None:
        """Удаляет объект Breed по его первичному ключу."""
        breed = self.get(pk)
        breed.delete()
