from django.contrib import admin

from dogs.models.breed import Breed
from dogs.models.dog import Dog


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    )
    list_display_links = (
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    )

    search_fields = (
        "name",
        "size",
    )
    ordering = (
        "name",
        "size",
    )

    filter_horizontal = ()


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
    )
    list_display_links = (
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
    )

    search_fields = (
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
    )
    ordering = ("name", "breed", "age")

    filter_horizontal = ()
