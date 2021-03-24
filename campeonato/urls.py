""" URLS del Campeonato"""

# Django Imports
from django.urls import path

# Project Imports
from campeonato.views import CampeonatoList, ClasificacionList
from partido.views import EncuentroList, GolesList

urlpatterns = [
    path(
        route = '<pk>/',
        view = CampeonatoList.as_view(),
        name = 'campeonato'
    ),

    path(
        route = '<pk>/clasificacion/', 
        view = ClasificacionList.as_view(), 
        name = 'clasificacion'
    ),

    path(
        route = '<pk>/fixture/', 
        view = EncuentroList.as_view(), 
        name = 'campeonato'
    ),

    path(
        route = '<pk>/goleadores/', 
        view = GolesList.as_view(), 
        name = 'goleadores'
    )
]