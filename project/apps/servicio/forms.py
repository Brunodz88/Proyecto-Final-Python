from django import forms
from django.contrib.auth.models import User

from .models import Obra, Comentario


class FormularioNuevaObra(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ("usuario", "titulo", "obra", "descripcion", "añodeejecución", "valor", "telefonoContacto", "emailContacto", "imagenObra")

        widgets = {
            "usuario": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "usuario_id", "type": "hidden"}),
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "Obra": forms.Select(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "añodeejecución": forms.TextInput(attrs={"class": "form-control"}),
            "valor": forms.TextInput(attrs={"class": "form-control"}),
            "telefonoContacto": forms.TextInput(attrs={"class": "form-control"}),
            "emailContacto": forms.TextInput(attrs={"class": "form-control"}),
        }


class ActualizacionObra(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ("titulo", "obra", "marca", "modelo", "descripcion", "year", "precio", "telefonoContacto", "emailContacto", "imagenObra")

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "obra": forms.Select(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "year": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "telefonoContacto": forms.TextInput(attrs={"class": "form-control"}),
            "emailContacto": forms.TextInput(attrs={"class": "form-control"}),
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("nombre", "mensaje")
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control"}),
        }
