""" Modelos para la APP equipo """

from django.db import models


class Equipo(models.Model):
    """Modelo que registra los equipos que participan
    en los torneos.

    Datos:
    - nombre (varchar)
    - logotipo (imagefield)
    """
    nombre_equipo = models.CharField(
        max_length = 80,
        help_text = 'Nombre del equipo participante',
        verbose_name = 'Nombre Equipo'
    )

    logo_equipo = models.ImageField(
        upload_to = 'logos_equipos', 
        blank = True,
        null=True,
        help_text = 'Logo del equipo',
        verbose_name = 'Logo / Imagen',
    )

    def __str__(self):
        return self.nombre_equipo

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

# class Jugador_Equipo(models.Model):
#     """Modelo intermedio para vincular a un jugador con su equipo
    
#     Datos:
#     - id_equipo (FK equipo)
#     """
#     id_equipo = models.ForeignKey(
#         'Equipo',
#         on_delete = models.CASCADE,
#         help_text = 'Nombre del equipo',
#         verbose_name = 'Equipo',
#     )

#     class Meta:
#         abstract = True

class Jugador(models.Model):
    """Modelo que registra los datos de un jugador

    Datos:
    - id_equipo (jugador_equipo)
    - apellido (varchar)
    - nombre (varchar)
    - numero (varchar)
    """
    id_equipo = models.ForeignKey(
        'Equipo',
        default = None,
        on_delete = models.CASCADE,
        help_text = 'Nombre del equipo',
        verbose_name = 'Equipo',
    )

    apellido = models.CharField(
        max_length = 80,
        help_text = 'Apellido del jugador',
        verbose_name = 'Apellido'
    )

    nombre = models.CharField(
        max_length = 80,
        blank = True,
        null=True,
        help_text = 'Nombre del jugador',
        verbose_name = 'Nombre'
    )

    numero = models.PositiveIntegerField(
        default = 0,
        blank = True,
        null=True,
        help_text = 'Numero de camiseta del jugador',
        verbose_name = 'Numero'
    )

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)


    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'