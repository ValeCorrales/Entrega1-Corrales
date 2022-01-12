from django import forms

class AlojamientoFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    tipoDeAlojamiento = forms.CharField(max_length=40)
    calificacion = forms.IntegerField()
    
class CiudadesFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    continente = forms.CharField(max_length=40)
    calificacion = forms.IntegerField()
    
    
class RestaurantesFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    tipoDeComida = forms.CharField(max_length=40)
    calificacion = forms.IntegerField()
    
#class ContactanosFormulario(forms.Form):
    
    #nombreYApellido = forms.CharField(max_length=40)
    #mail = forms.CharField(max_length=40)
    #numeroDeTelefono = forms.IntegerField()
    
    
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 