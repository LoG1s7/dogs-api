from typing import ClassVar

from rest_framework import serializers

from dogs.models.breed import Breed
from dogs.models.dog import Dog


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(),
        source="breed",
        write_only=True,
    )

    class Meta:
        model = Dog
        fields: ClassVar[list[str]] = [
            "id",
            "name",
            "age",
            "breed",
            "breed_id",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        ]
