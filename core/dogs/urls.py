from django.urls import path

from dogs.controllers.breed import (
    BreedListCreateView,
    BreedRetrieveUpdateDestroyView,
)
from dogs.controllers.dog import (
    DogListCreateView,
    DogRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("dogs/", DogListCreateView.as_view(), name="dog-list-create"),
    path(
        "dogs/<int:pk>/",
        DogRetrieveUpdateDestroyView.as_view(),
        name="dog-detail",
    ),
    path("breeds/", BreedListCreateView.as_view(), name="breed-list-create"),
    path(
        "breeds/<int:pk>/",
        BreedRetrieveUpdateDestroyView.as_view(),
        name="breed-detail",
    ),
]
