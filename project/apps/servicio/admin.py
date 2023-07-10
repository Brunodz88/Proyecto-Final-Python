from django.contrib import admin

from . import models

admin.site.site_title = "Servicio"
admin.site.site_header = "Proyectos Ingenieriles"


@admin.register(models.Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "titulo",
        "obra",
        "descripcion",
        "year",
        "precio",
        "fechaPublicacion",
        "telefonoContacto",
        "emailContacto",
        "imagenObra",
    )
    search_fields = (
        "usuario",
        "titulo",
        "obra",
        "descripcion",
        "year",
        "precio",
        "fechaPublicacion",
        "telefonoContacto",
        "emailContacto",
        "imagenObra",
    )
    list_filter = (
        "usuario",
        "titulo",
        "obra",
        "descripcion",
        "year",
        "precio",
        "fechaPublicacion",
        "telefonoContacto",
        "emailContacto",
        "imagenObra",
    )
    ordering = (
        "usuario",
        "titulo",
        "obra",
        "descripcion",
        "year",
        "precio",
        "fechaPublicacion",
        "telefonoContacto",
        "emailContacto",
        "imagenObra",
    )


@admin.register(models.Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        "comentario",
        "nombre",
        "mensaje",
        "fechaComentario",
    )

    search_fields = (
        "comentario",
        "nombre",
        "mensaje",
        "fechaComentario",
    )

    list_filter = (
        "comentario",
        "nombre",
        "mensaje",
        "fechaComentario",
    )

    ordering = (
        "comentario",
        "nombre",
        "mensaje",
        "fechaComentario",
    )
