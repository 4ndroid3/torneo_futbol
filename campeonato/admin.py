# Django Imports
from django.contrib import admin

# Project Imports
from campeonato.models import Campeonato, Clasificacion

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_campeonato', 'fecha_inicio', 'descripcion',)
    list_filter = ('nombre_campeonato',)
    search_fields = ('nombre_campeonato',)

class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('id_equipo', 'id_campeonato', 'puntos', 'partidos_jugados')
    list_filter = ('id_equipo', 'id_campeonato',)
    search_fields = ('id_equipo', 'id_campeonato',)
    ordering = ('-partidos_jugados', '-puntos', '-victorias', '-derrotas')

admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)