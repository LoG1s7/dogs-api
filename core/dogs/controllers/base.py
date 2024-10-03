from typing import Any, Generic, TypeVar

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

ModelType = TypeVar("ModelType")
ServiceType = TypeVar("ServiceType")
SerializerType = TypeVar("SerializerType")


class BaseListCreateView(generics.ListCreateAPIView, Generic[ModelType, ServiceType]):
    """Обобщенное представление для отображения списка и создания новых объектов."""

    service: ServiceType
    serializer_class: SerializerType

    def get_queryset(self) -> list[ModelType]:
        return self.service.list()

    def list(self, request, *args, **kwargs) -> Response:
        """Возвращает список объектов."""
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        """Создает новый объект на основе данных из запроса."""
        data = request.data
        obj = self.service.create(data)
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=HTTP_201_CREATED)


class BaseRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView, Generic[ModelType, ServiceType]
):
    """Обобщенное представление для получения, обновления или удаления объектов."""

    service: ServiceType
    serializer_class: type[Any]
    lookup_field = "pk"

    def get_object(self) -> ModelType:
        pk: int = self.kwargs["pk"]
        return self.service.get(pk)

    def retrieve(self, request, *args, **kwargs) -> Response:
        """Возвращает данные о конкретном объекте."""
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs) -> Response:
        """Обновляет данные о конкретном объекте на основе данных из запроса."""
        pk: int = kwargs["pk"]
        data: dict[str, Any] = request.data
        obj = self.service.update(pk, data)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs) -> Response:
        """Удаляет конкретный объект."""
        pk: int = kwargs["pk"]
        self.service.delete(pk)
        return Response(status=HTTP_204_NO_CONTENT)
