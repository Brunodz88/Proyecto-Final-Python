from django import views
from django.urls import path
from .views import (
    ObrascivilesDelete,
    ProyectoCreacion,
    ObrascivilesDetalle,
    ObrashidraulicasLista,
    ObrascivilesLista,
    ViasdecomunicacionLista,
    ObrashidraulicasDetalle,
    ViasdecomunicacionDetalle,
    ObrascivilesUpdate,
    ObrashidraulicasUpdate,
    ViasdecomunicacionUpdate,
    ObrashidraulicasDelete,
    ViasdecomunicacionDelete,
    ComentarioPagina,
)
from django.contrib.auth.views import LogoutView
from . import views

app_name = "servicio"

urlpatterns = [
    path("listaObrasciviles/", ObrascivilesLista.as_view(), name="obrasciviles"),
    path("listaObrashidraulicas/", ObrashidraulicasLista.as_view(), name="obrashidraulicas"),
    path("listaViasdecomunicacion/", ViasdecomunicacionLista.as_view(), name="viasdecomunicacion"),
    path("obrascivilesDetalle/<int:pk>/", ObrascivilesDetalle.as_view(), name="obrasciviles_detalle"),
    path("obrashidraulicasDetalle/<int:pk>/", ObrashidraulicasDetalle.as_view(), name="obrashidraulicas_detalle"),
    path("viasdecomunicacionDetalle/<int:pk>/", ViasdecomunicacionDetalle.as_view(), name="viasdeocomunicacion_detalle"),
    path("obrascivilesEdicion/<int:pk>/", ObrascivilesUpdate.as_view(), name="obrasciviles_editar"),
    path("obrashidraulicasEdicion/<int:pk>/", ObrashidraulicasUpdate.as_view(), name="obrashidraulicas_editar"),
    path("viasdecomunicacionEdicion/<int:pk>/", ViasdecomunicacionUpdate.as_view(), name="viasdecomunicacion_editar"),
    path("obrascivilesBorrado/<int:pk>/", ObrascivilesDelete.as_view(), name="obrasciviles_eliminar"),
    path("obrashidraulicasBorrado/<int:pk>/", ObrashidraulicasDelete.as_view(), name="obrashidraulicas_eliminar"),
    path("viasdecomunicacionBorrado/<int:pk>/", ViasdecomunicacionDelete.as_view(), name="viasdecomunicacion_eliminar"),
    path("proyectoCreacion/", ProyectoCreacion.as_view(), name="proyectoCreacion"),
    path("obrascivilesDetalle/<int:pk>/comentario/", ComentarioPagina.as_view(), name="comentario"),
    path("obrashidraulicasDetalle/<int:pk>/comentario/", ComentarioPagina.as_view(), name="comentario"),
    path("viasdecomunicacionDetalle/<int:pk>/comentario/", ComentarioPagina.as_view(), name="comentario"),
]
