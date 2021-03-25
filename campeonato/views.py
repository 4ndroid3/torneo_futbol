""" Contiene los views del Campeonato"""

# Django Imports
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

# Project Imports
from campeonato.models import Clasificacion, Campeonato

class CampeonatoList(DetailView):
    """ Lista la tabla de clasificacion del campeonato"""
    model = Campeonato
    template_name = 'campeonato/templates/inicio/index.html'

class ClasificacionList(ListView):
    """ Lista la tabla de clasificacion del campeonato"""
    model = Clasificacion
    template_name = 'campeonato/templates/campeonato/clasificacion_list.html'
    ordering = ('-puntos', '-partidos_jugados')