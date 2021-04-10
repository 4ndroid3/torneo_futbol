# Django Imports
from django.contrib import admin

# Project Imports
from partido.models import Partido, Encuentro, Sede, Goles

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('id_encuentro', 'goles_eq1', 'goles_eq2')
    list_filter = ('id_encuentro__id_equipo1','id_encuentro__id_equipo2')

class EncuentroAdmin(admin.ModelAdmin):
    list_display = ('id_equipo1', 'id_equipo2', 'id_sede', 'id_campeonato', 'fecha_encuentro', 'estado')
    list_filter = ('id_sede', 'id_campeonato', 'estado')
    search_fields = ('id_sede', 'id_campeonato', 'estado', 'id_equipo1', 'id_equipo2')

class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre_sede',)
    list_filter = ('nombre_sede',)

class GolesAdmin(admin.ModelAdmin):
    list_display = ('id_jugador', 'id_partido')
    list_filter = ('id_jugador', 'id_partido')
    search_fields = ('id_jugador', 'id_partido')

admin.site.register(Partido, PartidoAdmin)
admin.site.register(Encuentro, EncuentroAdmin)
admin.site.register(Sede, SedeAdmin)
admin.site.register(Goles, GolesAdmin)