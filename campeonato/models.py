""" Modelos para la APP campeonato """

from django.db import models

class Campeonato(models.Model):
    """Modelo campeonato registra los datos principales
    del campeonato que se está jugando.

    Datos:
    - nombre (charvar)
    - FechaInicio (datefield)
    - descripcion (text)
    - id_equipo (FK equipo)
    """
    pass

class Clasificacion(models.Model):
    """Modelo clasificación registra los datos que obtienen
    los equipos a lo largo de la competicion.

    Datos:
    - id_equipo (FK de equipo)
    - id_campeonato (FK de campeonato)
    - puntos (integer)
    - partidos_jugados (positive integer)
    - victorias (positive integer)
    - derrotas (positive integer)
    - empates (positive integer)
    - goles_favor (positive integer)
    - goles_contra (positive integer)

    """
    pass