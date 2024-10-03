from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.request import Request


class CustomExceptionMiddleware:
    """Пользовательский middleware для обработки исключений в Django REST framework.
    Этот middleware перехватывает и обрабатывает определенные исключения,
    которые могут возникнуть во время цикла запрос-ответ.
    Он возвращает соответствующие ответы JSON с соответствующими кодами HTTP-статуса.
    """

    def __init__(self, get_response):
        """Инициализирует middleware с вызываемым объектом следующего middleware.

        Args:
            get_response (callable): Следующий middleware.

        """
        self.get_response = get_response

    def __call__(self, request: Request):
        """Обрабатывает входящий запрос и вызывает следующий middleware в стеке.

        Returns:
            Response: Ответ от следующего middleware.

        """
        try:
            return self.get_response(request)
        except ValidationError as ve:
            return JsonResponse({"errors": ve.message_dict}, status=400)
        except NotFound as nf:
            return JsonResponse({"detail": nf.default_detail}, status=404)
        except PermissionDenied as pd:
            return JsonResponse({"detail": pd.default_detail}, status=403)
        except IntegrityError as ie:
            return JsonResponse(
                {"detail": "Ошибка целостности.", "errors": str(ie)},
                status=400,
            )
