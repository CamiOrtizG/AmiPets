from django import forms
from django.forms.widgets import DateInput
from .models import Persona, ficha_pet, Funcionario, reserva, estadia, Vacuna


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ["rut", "dv", "nombres", "phone", "mail", "direccion", "comuna"]



class FichapetForm(forms.ModelForm):

    class Meta:
        model = ficha_pet
        fields = '__all__'

# Revisar si se debe modificar esta clase y poner específicamente los campos que debemos llamar en el formulario
 
class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = '__all__' 
# Revisar si se debe modificar esta clase y poner específicamente los campos que debemos llamar en el formulario


class ReservaForm(forms.ModelForm):

    class Meta:
        model = reserva
        fields = ["estado", "persona", "fecha_ini", "fecha_term", "descrip"]
        #fields = '__all__' 
        widgets = {
            "fecha_ini": DateInput(attrs={'type': 'date'}),
            "fecha_term": DateInput(attrs={'type': 'date'})
        },

class EstadiaForm(forms.ModelForm):

    class Meta:
        model = estadia
        fields = '__all__'
        widgets = {
            "fech_pago": DateInput(attrs={'type': 'date'})
        },

class VacunaForm(forms.ModelForm):

    class Meta:
        model = Vacuna
        fields = '__all__' 