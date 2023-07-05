from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Obra, Comentario
from .forms import ActualizacionObra, FormularioNuevaObra, FormularioComentario


# OBRAS CIVILES


class ObrascivilesLista(LoginRequiredMixin, ListView):
    context_object_name = "obrasciviles"
    queryset = Obra.objects.filter(obra__startswith="obrasciviles")
    template_name = "servicio/listaObrasciviles.html"
    login_url = "/login/"


class ObrascivilesDetalle(LoginRequiredMixin, DetailView):
    model = Obra
    context_object_name = "obrasciviles"
    template_name = "servicio/obrascivilesDetalle.html"


class ObrascivilesUpdate(LoginRequiredMixin, UpdateView):
    model = Obra
    form_class = ActualizacionObra
    success_url = reverse_lazy("obrasciviles")
    context_object_name = "obrasciviles"
    template_name = "servicio/obrascivilesEdicion.html"


class ObrascivilesDelete(LoginRequiredMixin, DeleteView):
    model = Obra
    success_url = reverse_lazy("obrasciviles")
    context_object_name = "obrasciviles"
    template_name = "servicio/obrascivilesBorrado.html"


# OBRAS HIDRAULICAS


class ObrashidraulicasLista(LoginRequiredMixin, ListView):
    context_object_name = "obrashidraulicas"
    queryset = Obra.objects.filter(obra__startswith="obrashidraulicas")
    template_name = "servicio/listaObrashidraulicas.html"


class ObrashidraulicasDetalle(LoginRequiredMixin, DetailView):
    model = Obra
    context_object_name = "obrashidraulicas"
    template_name = "servicio/obrashidraulicasDetalle.html"


class ObrashidraulicasUpdate(LoginRequiredMixin, UpdateView):
    model = Obra
    form_class = ActualizacionObra
    success_url = reverse_lazy("Obrashidraulicas")
    context_object_name = "Obrashidraulicas"
    template_name = "servicio/obrashidraulicasEdicion.html"


class ObrashidraulicasDelete(LoginRequiredMixin, DeleteView):
    model = Obra
    success_url = reverse_lazy("obrashidraulicas")
    context_object_name = "obrashidraulicas"
    template_name = "servicio/obrashidraulicasBorrado.html"


# VIAS DE COMUNICACION


class ViasdecomunicacionLista(LoginRequiredMixin, ListView):
    context_object_name = "viasdecomunicacion"
    queryset = Obra.objects.filter(obra__startswith="viasdecomunicacion")
    template_name = "servicio/listaViasdecomunicacion.html"


class ViasdecomunicacionDetalle(LoginRequiredMixin, DetailView):
    model = Obra
    context_object_name = "viasdecomunicacion"
    template_name = "servicio/viasdecomunicacionDetalle.html"


class ViasdecomunicacionUpdate(LoginRequiredMixin, UpdateView):
    model = Obra
    form_class = ActualizacionObra
    success_url = reverse_lazy("Viasdecomunicacion")
    context_object_name = "viasdecomunicacion"
    template_name = "servicio/viasdecomunicacionEdicion.html"


class ViasdecomunicacionDelete(LoginRequiredMixin, DeleteView):
    model = Obra
    success_url = reverse_lazy("viasdecomunicacion")
    context_object_name = "viasdecomunicacion"
    template_name = "servicio/viasdecomunicacionBorrado.html"


# CREACION INSTRUMENTO


class ProyectoCreacion(LoginRequiredMixin, CreateView):
    model = Obra
    form_class = FormularioNuevaObra
    success_url = reverse_lazy("servicio")
    template_name = "servicio/proyectoCreacion.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProyectoCreacion, self).form_valid(form)


# COMENTARIOS


class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = "servicio/comentario.html"
    success_url = reverse_lazy("servicio")

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs["pk"]
        return super(ComentarioPagina, self).form_valid(form)
