""" Modelos para la APP campeonato """
# Django Imports
from django.db import models

# Project Imports
from equipo.models import Equipo

class Campeonato(models.Model):
    """Modelo campeonato registra los datos principales
    del campeonato que se está jugando.

    Datos:
    - nombre (charvar)
    - FechaInicio (datefield)
    - descripcion (text)
    - id_equipo (FK equipo)
    """
    nombre_campeonato = models.CharField(
        default = '',
        max_length = 80,
        help_text = 'Nombre del campeonato',
        verbose_name = 'Nombre Campeonato'
    )

    fecha_inicio = models.DateField(
        blank = True,
        null=True,
        verbose_name = 'Fecha Inicio',
        help_text = 'Fecha en la que inició el campeonato',
    )

    descripcion = models.TextField(
        default = '',
        max_length = 250,
        help_text = 'Descripcion',
        verbose_name = 'Descripcion del campeonato'
    )

    id_equipo = models.ForeignKey(
        Equipo,
        default = 0,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
        help_text = 'Nombre del equipo',
        verbose_name = 'Id_delequipo',
    )

    def __str__(self):
        return self.nombre_campeonato

    class Meta:
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'


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
    id_equipo = models.ForeignKey(
        Equipo,
        default = 0,
        on_delete = models.CASCADE,
        help_text = 'Nombre del equipo',
        verbose_name = 'Equipo',
    )

    id_campeonato = models.ForeignKey(
        'Campeonato',
        default = 0,
        on_delete = models.CASCADE,
        help_text = 'Nombre del Campeonato',
        verbose_name = 'Campeonato',
    )

    puntos = models.IntegerField(
        default = 0, 
        help_text = 'Puntos acumulados por equipo',
        verbose_name = 'Puntos',
    )

    partidos_jugados = models.PositiveIntegerField(
        default=0, 
        help_text = 'Partidos jugados por el equipo en el campeonato',
        verbose_name = 'Partidos Jugados',
    )

    victorias = models.PositiveIntegerField(
        default=0, 
        help_text = 'Victorias del equipo en el campeonato',
        verbose_name = 'Victorias',
    )

    derrotas = models.PositiveIntegerField(
        default=0, 
        help_text = 'Derrotas del equipo en el campeonato',
        verbose_name = 'Derrotas',
    )

    empates = models.PositiveIntegerField(
        default=0, 
        help_text = 'Empates del equipo en el campeonato',
        verbose_name = 'Empates',
    )

    goles_favor = models.PositiveIntegerField(
        default=0, 
        help_text = 'Goles convertidos por el equipo en el campeonato',
        verbose_name = 'Goles a favor',
    )

    goles_contra = models.PositiveIntegerField(
        default=0, 
        help_text = 'Goles que le convirtieron al equipo en el campeonato',
        verbose_name = 'Goles en contra',
    )

    def __str__(self):
        return self.id_equipo

    class Meta:
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciones'