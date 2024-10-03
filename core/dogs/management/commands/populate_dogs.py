import random
from faker import Faker
from django.core.management.base import BaseCommand

from dogs.models.breed import Breed
from dogs.models.dog import Dog

fake = Faker()


class Command(BaseCommand):
    help = 'Заполняет базы данных данными для моделей Breed и Dog'

    def handle(self, *args, **kwargs):
        breeds = [
            {
                "name": "Лабрадор",
                "size": Breed.Sizes.LARGE,
                "friendliness": random.randint(1, 5),
                "trainability": random.randint(1, 5),
                "shedding_amount": random.randint(1, 5),
                "exercise_needs": random.randint(1, 5),
            },
            {
                "name": "Бигль",
                "size": Breed.Sizes.SMALL,
                "friendliness": random.randint(1, 5),
                "trainability": random.randint(1, 5),
                "shedding_amount": random.randint(1, 5),
                "exercise_needs": random.randint(1, 5),
            },
            {
                "name": "Немецкая Овчарка",
                "size": Breed.Sizes.LARGE,
                "friendliness": random.randint(1, 5),
                "trainability": random.randint(1, 5),
                "shedding_amount": random.randint(1, 5),
                "exercise_needs": random.randint(1, 5),
            },
            {
                "name": "Пудель",
                "size": Breed.Sizes.MEDIUM,
                "friendliness": random.randint(1, 5),
                "trainability": random.randint(1, 5),
                "shedding_amount": random.randint(1, 5),
                "exercise_needs": random.randint(1, 5),
            },
            {
                "name": "Бульдог",
                "size": Breed.Sizes.MEDIUM,
                "friendliness": random.randint(1, 5),
                "trainability": random.randint(1, 5),
                "shedding_amount": random.randint(1, 5),
                "exercise_needs": random.randint(1, 5),
            },
            {
                "name": "Йокширский терьер",
                "size": Breed.Sizes.TINY,
                "friendliness": random.randint(1, 5),
                "trainability": random.randint(1, 5),
                "shedding_amount": random.randint(1, 5),
                "exercise_needs": random.randint(1, 5),
            },
        ]

        for breed_data in breeds:
            breed = Breed.objects.create(**breed_data)
            self.stdout.write(f'Добавлена порода: {breed.name}')

            for _ in range(random.randint(5, 10)):
                dog = Dog.objects.create(
                    name=fake.first_name(),
                    age=random.randint(1, 15),
                    breed=breed,
                    gender=random.choice([Dog.Gender.MALE, Dog.Gender.FEMALE]),
                    color=fake.color_name(),
                    favorite_food=fake.word(),
                    favorite_toy=fake.word(),
                )
                self.stdout.write(f'Добавлена собака: {dog.name}')
