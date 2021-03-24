""" Contiene los views del Campeonato"""

# Django Imports
from django.shortcuts import render
from django.views.generic import ListView

# Project Imports
from campeonato.models import Clasificacion

class CampeonatoList(ListView):
    """ Lista la tabla de clasificacion del campeonato"""
    model = Clasificacion
    template_name = 'campeonato/templates/campeonato/clasificacion_list.html'
    ordering = 'puntos'