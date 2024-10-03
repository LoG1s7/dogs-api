from abc import ABC, abstractmethod
from typing import Any


class BaseRepositoryInterface(ABC):
    @abstractmethod
    def list(self, *args, **kwargs) -> list[Any]:
        pass

    @abstractmethod
    def create(self, data: dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def get(self, pk: int) -> Any:
        pass

    @abstractmethod
    def update(self, pk: int, data: dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def delete(self, pk: int) -> None:
        pass
