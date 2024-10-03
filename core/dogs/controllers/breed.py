from dogs.controllers.base import BaseListCreateView, BaseRetrieveUpdateDestroyView
from dogs.models.breed import Breed
from dogs.repositories.breed_repository import BreedRepository
from dogs.serializers import BreedSerializer
from dogs.services.breed_service import BreedService

breed_service = BreedService(repository=BreedRepository())


class BreedListCreateView(BaseListCreateView[Breed, BreedService]):
    """View для отображения списка пород или создания новой породы."""

    service = BreedService(repository=BreedRepository())
    serializer_class = BreedSerializer


class BreedRetrieveUpdateDestroyView(
    BaseRetrieveUpdateDestroyView[Breed, BreedService]
):
    """View для получения, обновления или удаления экземпляров породы собаки."""

    service = BreedService(repository=BreedRepository())
    serializer_class = BreedSerializer
