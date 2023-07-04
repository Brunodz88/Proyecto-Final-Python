from django import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, RegistroPagina, UsuarioEdicion, CambioPassword
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("registro/", RegistroPagina.as_view(), name="registro"),
    path("edicionPerfil/", UsuarioEdicion.as_view(), name="edicion"),
    path("passwordCambio/", CambioPassword.as_view(), name="cambio_password"),
    path("passwordExitoso/", views.password_exitoso, name="cambio_exitoso"),
    path("about/", views.about, name="about"),
]
