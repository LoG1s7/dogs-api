from dogs.controllers.base import BaseListCreateView, BaseRetrieveUpdateDestroyView
from dogs.models.dog import Dog
from dogs.repositories.dog_repository import DogRepository
from dogs.serializers import DogSerializer
from dogs.services.dog_service import DogService


class DogListCreateView(BaseListCreateView[Dog, DogService]):
    """View для отображения списка собак или создания новой собаки."""

    service = DogService(repository=DogRepository())
    serializer_class = DogSerializer


class DogRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView[Dog, DogService]):
    """View для получения, обновления или удаления экземпляров собаки."""

    service = DogService(repository=DogRepository())
    serializer_class = DogSerializer
