from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView

from .forms import (
    FormularioCambioPassword,
    FormularioEdicion,
    FormularioRegistroUsuario,
)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


class LoginPagina(LoginView):
    template_name = "home/login.html"
    fields = "__all__"
    redirect_autheticated_user = True
    success_url = reverse_lazy("home:index")

    def get_success_url(self):
        return reverse_lazy("home:index")


class RegistroPagina(FormView):
    template_name = "home/registro.html"
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home:index")
        return super(RegistroPagina, self).get(*args, **kwargs)


class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name = "home/edicionPerfil.html"
    success_url = reverse_lazy("home:index")

    def get_object(self):
        return self.request.user


class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = "home/passwordCambio.html"
    success_url = reverse_lazy("home:passwordExitoso")


def password_exitoso(request):
    return render(request, "home:passwordExitoso", {})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "home/about.html")
