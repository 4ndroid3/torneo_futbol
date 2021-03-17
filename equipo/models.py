""" Modelos para la APP equipo """

from django.db import models


class Equipo(models.Model):
    """Modelo que registra los equipos que participan
    en los torneos.

    Datos:
    - nombre (varchar)
    - logotipo (imagefield)
    """
    pass

class Jugador_Equipo(models.Model):
    """Modelo intermedio para vincular a un jugador con su equipo
    
    Datos:
    - id_equipo (FK equipo)
    """
    pass

class Jugador(models.Model):
    """Modelo que registra los datos de un jugador

    Datos:
    - apellido (varchar)
    - nombre (varchar)
    - numero (varchar)
    """
    pass