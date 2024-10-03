from dogs.models.dog import Dog
from dogs.repositories.dog_repository import DogRepository
from dogs.services.base_service import BaseService


class DogService(BaseService[Dog, DogRepository]):
    """Сервис для управления моделью Dog."""
