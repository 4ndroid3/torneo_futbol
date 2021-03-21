# Django Imports
from django.contrib import admin

# Project Imports
from equipo.models import Equipo, Jugador

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre_equipo',)
    list_filter = ('nombre_equipo',)
    search_fields = ('nombre_equipo',)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'numero', 'id_equipo')
    list_filter = ('apellido', 'nombre', 'id_equipo')
    search_fields = ('apellido', 'nombre', 'numero', 'id_equipo')
    ordering  = ('id_equipo',)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)