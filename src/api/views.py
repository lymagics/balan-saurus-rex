from django.conf import settings
from django.http import HttpResponse, JsonResponse


def index_route(request: HttpResponse):
    """
    API index route. Returns API_NAME variable.
    """
    return JsonResponse({'name': settings.API_NAME})
