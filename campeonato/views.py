""" Contiene los views del Campeonato"""

# Django Imports
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

# Project Imports
from campeonato.models import Clasificacion, Campeonato

def index(request):

    context = {

    }

    return render(request, 'inicio/index.html', context)

class CampeonatoList(DetailView):
    """ Lista la tabla de clasificacion del campeonato"""
    model = Campeonato

class ClasificacionList(ListView):
    """ Lista la tabla de clasificacion del campeonato"""
    model = Clasificacion
    template_name = 'campeonato/templates/campeonato/clasificacion_list.html'
    ordering = ('-puntos', '-partidos_jugados')