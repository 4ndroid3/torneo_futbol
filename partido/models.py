""" Modelos para la APP partido """
# Django Imports
from django.db import models

# Project Imports
from equipo.models import Equipo, Jugador
from campeonato.models import Campeonato


class Partido(models.Model):
    """
    Datos:
    - id_encuentro (FK de encuentro)
    - goles_eq1 (positive int)
    - goles_eq2 (positive int)
    """
    id_encuentro = models.ForeignKey(
        'Encuentro',
        default = 0,
        on_delete = models.CASCADE,
        help_text = 'Datos del encuentro',
        verbose_name = 'Encuentro',
    )

    goles_eq1 = models.PositiveIntegerField(
        default=0, 
        help_text = 'Goles del equipo 1',
        verbose_name = 'Goles Equipo 1',
    )

    goles_eq2 = models.PositiveIntegerField(
        default=0, 
        help_text = 'Goles del equipo 2',
        verbose_name = 'Goles Equipo 2',
    )

    def __str__(self):
        return str(self.id_encuentro)

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'

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
    id_equipo1 = models.ForeignKey(
        Equipo,
        default = None,
        on_delete = models.CASCADE,
        related_name = 'equipo1',
        help_text = 'Datos del equipo que jugó el partido',
        verbose_name = 'Equipo N°1',
    )

    id_equipo2 = models.ForeignKey(
        Equipo,
        default = None,
        on_delete = models.CASCADE,
        related_name = 'equipo2',
        help_text = 'Datos del equipo que jugó el partido',
        verbose_name = 'Equipo N°2',
    )

    id_sede = models.ForeignKey(
        'Sede',
        default = None,
        on_delete = models.CASCADE,
        help_text = 'Sede en la que se jugó el encuentro',
        verbose_name = 'Sede',
    )

    id_campeonato = models.ForeignKey(
        Campeonato,
        default = None,
        on_delete = models.CASCADE,
        help_text = 'Nombre del campeonato que se está jugando',
        verbose_name = 'Campeonato',
    )

    fecha_encuentro = models.DateField(
        blank = True,
        null=True,
        verbose_name = 'Fecha del Encuentro',
        help_text = 'Fecha en la que se jugó el partido',
    )

    ESTADOS = (
        ('P', 'Por Jugar'),
        ('J', 'Jugado'),
        ('S', 'Suspendido'),
    )

    estado = models.CharField(
        default = 'P',
        max_length = 1,
        choices = ESTADOS,
    )

    def __str__(self):
        return '{} vs {}'.format(self.id_equipo1, self.id_equipo2)

    class Meta:
        verbose_name = 'Encuentro'
        verbose_name_plural = 'Encuentros'

class Sede(models.Model):
    """
    Datos:
    - nombre (charfield)
    """
    nombre_sede = models.CharField(
        default = '',
        max_length = 80, 
        help_text = 'Sede donde se juega el partido',
        verbose_name = 'Nombre Sede',
    )

    def __str__(self):
        return self.nombre_sede

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

class Goles(models.Model):
    """
    Datos:
    - id_jugador (FK jugador)
    - id_partido (FK partido)
    """
    id_jugador = models.ForeignKey(
        Jugador,
        default = 0,
        on_delete = models.CASCADE,
        help_text = 'Gol anotado por el jugador',
        verbose_name = 'Jugador',
    )

    id_partido = models.ForeignKey(
        'Partido',
        default = 0,
        on_delete = models.CASCADE,
        help_text = 'Partido donde se convirtio el gol',
        verbose_name = 'Partido',
    )

    def __str__(self):
        return str(self.id_jugador)

    class Meta:
        verbose_name = 'Gol'
        verbose_name_plural = 'Goles'