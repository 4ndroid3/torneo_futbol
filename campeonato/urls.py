""" URLS del Campeonato"""

# Django Imports
from django.urls import path

# Project Imports
from campeonato.views import CampeonatoList

urlpatterns = [
    path(route = '', view = CampeonatoList.as_view(), name = 'campeonato'),
]