from django.urls import path

from api.views import index_route

urlpatterns = [
    path('', index_route, name='index'),
]

app_name = 'api'
