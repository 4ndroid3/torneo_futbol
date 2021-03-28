""" Contiene los views de los partidos"""

# Django Imports
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Sum, Count

# Project Imports
from partido.models import Encuentro, Goles

class EncuentroList(ListView):
    """ Lista de los partidos programados para jugar"""
    model = Encuentro
    template_name = 'partido/templates/partido/encuentro_list.html'
    ordering = 'fecha_encuentro'

class GolesList(ListView):
    """ Lista de los jugadores con más goles"""
    model = Goles
    template_name = 'partido/templates/partido/goles_list.html'
    ordering = 'id_jugador'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_goles'] = Goles.objects.values('id_jugador__apellido','id_jugador__nombre', 'id_jugador__id_equipo__nombre_equipo').annotate(cant_goles = Count('id_jugador')).order_by('-cant_goles')

        return context