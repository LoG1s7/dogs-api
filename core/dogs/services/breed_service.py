from dogs.models.breed import Breed
from dogs.repositories.breed_repository import BreedRepository
from dogs.services.base_service import BaseService


class BreedService(BaseService[Breed, BreedRepository]):
    """Сервис для управления моделью Breed."""
