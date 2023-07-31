from django.conf import settings
from django.http import HttpRequest, JsonResponse


def index_route(request: HttpRequest):
    """
    API index route. Returns API_NAME variable.
    """
    return JsonResponse({'name': settings.API_NAME})
