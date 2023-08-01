from recipes.views import contato, home, sobre
from django.urls import path, include


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato', contato),
]