""" Modelos para la APP partido """

from django.db import models


class Partido(models.Model):
    """
    Datos:
    - id_encuentro (FK de encuentro)
    - goles_eq1 (positive int)
    - goles_eq2 (positive int)
    """
    pass

class Encuentro(models.Model):
    """
    Datos:
    - id_equipo1 (FK equipo)
    - id_equipo2 (FK equipo)
    - id_sede (FK sede)
    - id_competicion (FK competicion)
    - fecha (datefield)
    - estado (boolean)
    """
    pass

class Sede(models.Model):
    """
    Datos:
    - nombre (charfield)
    """
    pass

class Goles(models.Model):
    """
    Datos:
    - id_jugador (FK jugador)
    - id_partido (FK partido)
    """
    pass