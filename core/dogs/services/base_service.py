from typing import Generic, TypeVar

from dogs.repositories.base_repository import BaseRepositoryInterface

ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType", bound=BaseRepositoryInterface)


class BaseService(Generic[ModelType, RepositoryType]):
    """Общий базовый класс для сервисов."""

    def __init__(self, repository: RepositoryType) -> None:
        """Инициализирует сервис с экземпляром репозитория."""
        self.repository = repository

    def list(self) -> list[ModelType]:
        """Получает список всех объектов из репозитория."""
        return self.repository.list()

    def create(self, data: dict) -> ModelType:
        """Создает новый объект в репозитории с указанными данными."""
        return self.repository.create(data)

    def get(self, pk: int) -> ModelType:
        """Получает объект из репозитория по указанному первичному ключу."""
        return self.repository.get(pk)

    def update(self, pk: int, data: dict) -> ModelType:
        """Обновляет существующий объект в репозитории с указанными данными."""
        return self.repository.update(pk, data)

    def delete(self, pk: int) -> None:
        """Удаляет объект из репозитория по указанному первичному ключу."""
        self.repository.delete(pk)
