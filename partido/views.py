""" Contiene los views de los partidos"""

# Django Imports
from django.shortcuts import render
from django.views.generic import ListView

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