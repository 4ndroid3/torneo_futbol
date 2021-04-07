""" URLS del Campeonato"""

# Django Imports
from django.urls import path

# Project Imports
from campeonato.views import CampeonatoDetail, ClasificacionList, CampeonatoList
from partido.views import EncuentroList, GolesList

urlpatterns = [
    path(
        route = '',
        view = CampeonatoList.as_view(),
        name = 'campeonato_list'
    ),
    path(
        route = '<pk>/',
        view = CampeonatoDetail.as_view(),
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
        name = 'fixture'
    ),

    path(
        route = '<pk>/goleadores/', 
        view = GolesList.as_view(), 
        name = 'goleadores'
    )
]