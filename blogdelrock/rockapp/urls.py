from django.urls import path
from .views import *


urlpatterns = [
    path("artistas/", artistas, name="artistas"),
    path("bandas/", bandas, name="bandas"),
    path("albums/", albums, name="albums"),
    path("", inicio, name="inicio"),
]