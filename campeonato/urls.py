""" URLS del Campeonato"""

# Django Imports
from django.urls import path

# Project Imports
from campeonato.views import CampeonatoList
from partido.views import EncuentroList, GolesList

urlpatterns = [
    path(
        route = 'clasificacion/', 
        view = CampeonatoList.as_view(), 
        name = 'clasificacion'
    ),

    path(
        route = 'fixture/', 
        view = EncuentroList.as_view(), 
        name = 'campeonato'
    ),

    path(
        route = 'goleadores/', 
        view = GolesList.as_view(), 
        name = 'goleadores'
    )
]