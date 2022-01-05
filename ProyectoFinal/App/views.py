from django.http.response import ResponseHeaders
from django.shortcuts import render
from django.http import HttpResponse
from App.models import Ciudades, Restaurantes, Alojamientos, Comentario
from App.forms import AlojamientoFormulario, RestaurantesFormulario, CiudadesFormulario, ContactanosFormulario, UserRegisterForm


# Create your views here.


def inicio(request):
    #return HttpResponse("Esto es una prueba de inicio") - Ok funciono
    
    return render(request, 'App/inicio.html')

def ciudades(request):
 
    return render(request, 'App/ciudades.html')

def restaurantes(request):
    
    return render(request, 'App/restaurantes.html')

def alojamientos(request):
    
    return render(request, 'App/alojamientos.html')

def contactanos(request):
    
    return render(request, 'App/contactanos.html')

#def alojamientoFormulario(request):
    
    #return render(request, 'App/alojamientoFormulario.html') - lo hacemos con django
    if request.method == "POST":
        miFormulario = AlojamientoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            alojamiento = Alojamientos(nombre=informacion['nombre'], tipoDeAlojamiento=informacion['tipoDeAlojamiento'], calificacion=informacion['calificacion'])
            
            alojamiento.save()
            
            return render(request, "App/alojamientos.html")
        
    else:
        miFormulario = AlojamientoFormulario()
        return render(request, "App/alojamientoFormulario.html", {"miFormulario":miFormulario})
    
    
#def ciudadesFormulario(request):
    
    if request.method == "POST":
        miFormulario2 = CiudadesFormulario(request.POST)
        print(miFormulario2)
        
        if miFormulario2.is_valid():
            informacion = miFormulario2.cleaned_data
            ciudades = Ciudades(nombre=informacion['nombre'], pais=informacion['pais'], continente=informacion['continente'] ,calificacion=informacion['calificacion'])
            
            ciudades.save()
            
            return render(request, "App/ciudades.html")
        
    else:
        miFormulario2 = CiudadesFormulario()
        return render(request, "App/ciudadesFormulario.html", {"miFormulario2":miFormulario2})
 
    
#def restaurantesFormulario(request):
    

    if request.method == "POST":
        miFormulario3 = RestaurantesFormulario(request.POST)
        print(miFormulario3)
        
        if miFormulario3.is_valid():
            informacion = miFormulario3.cleaned_data
            restaurantes = Restaurantes(nombre=informacion['nombre'], tipoDeComida=informacion['tipoDeComida'] ,calificacion=informacion['calificacion'])
            
            restaurantes.save()
            
            return render(request, "App/restaurantes.html")
        
    else:
        miFormulario3 = RestaurantesFormulario()
        return render(request, "App/restaurantesFormulario.html", {"miFormulario3":miFormulario3})
    
def contactanosFormulario(request):
    
    if request.method == "POST":
        miFormulario4 = ContactanosFormulario(request.POST)
        print(miFormulario4)
        
        if miFormulario4.is_valid():
            informacion = miFormulario4.cleaned_data
            contactanos = Comentario(nombreYApellido=informacion['nombreYApellido'], mail=informacion['mail'] ,numeroDeTelefono=informacion['numeroDeTelefono'])
            
            contactanos.save()
            
            return render(request, 'App/inicio.html')
        
    else:
        miFormulario4 = ContactanosFormulario()
        return render(request, "App/contactanos.html", {"miFormulario4":miFormulario4})
    
#segunda entrega

def about(request):
        
    return render(request, 'App/about.html')

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

#Leer
class CiudadesList(ListView):
        
   model = Ciudades
   template_name = "App/ciudades_list.html"

#Detalle - "leer mas"
class CiudadesDetalle(DetailView):
        
    model = Ciudades
    template_name = "App/ciudades_detalle.html"
    
#Crear elementos
class CiudadesCreacion(CreateView): #hacer ciudades_form.html
    
    model = Ciudades
    success_url = "../ciudades/list" # cuando terminas de crear la ciudad volve a la lista de ciudades
    fields = ["nombre", "pais", "continente", "calificacion"] #estos son los elementos que quiero que se carguen
    
#Modificar: update
class CiudadesUpdate(UpdateView): #este te lleva al ciudades_form tambien
       
    model = Ciudades
    success_url = "../ciudades/list"
    fields = ["nombre", "pais", "continente", "calificacion"]
    
#Borrar
class CiudadesDelete(DeleteView): #hacer ciudades_confirm_delete    
    
    model = Ciudades
    success_url = "../ciudades/list" 
    
class RestaurantesList(ListView):
        
    model = Restaurantes
    template_name = "AppC/restaurantes_list.html"
    

#Detalle - "leer mas"
class RestaurantesDetalle(DetailView):
        
    model = Restaurantes
    template_name = "App/restaurantes_detalle.html"
    
#Crear elementos
class RestaurantesCreacion(CreateView): 
    
    model = Restaurantes
    success_url = "../restaurantes/list" 
    fields = ["nombre", "tipoDeComida", "calificacion"] #estos son los elementos que quiero que se carguen
    
#Modificar: update
class RestaurantesUpdate(UpdateView):
       
    model = Restaurantes
    success_url = "../restaurantes/list"
    fields = ["nombre", "tipoDeComida", "calificacion"]
    
#Borrar
class RestaurantesDelete(DeleteView):   
    
    model = Restaurantes
    success_url = "../restaurantes/list" 

class AlojamientosList(ListView):
    model = Alojamientos
    template_name = "App/alojamientos_list.html"
    
    #Detalle - "leer mas"
class AlojamientosDetalle(DetailView):
        
    model = Alojamientos
    template_name = "App/alojamientos_detalle.html"
    
#Crear elementos
class AlojamientosCreacion(CreateView): 
    
    model = Alojamientos
    success_url = "../alojamientos/list" 
    fields = ["nombre", "tipoDeAlojamiento", "calificacion"] #estos son los elementos que quiero que se carguen
    
#Modificar: update
class AlojamientosUpdate(UpdateView): 
       
    model = Alojamientos
    success_url = "../alojamientos/list"
    fields = ["nombre", "tipoDeAlojamiento", "calificacion"]
    
#Borrar
class AlojamientosDelete(DeleteView):   
    
    model = Alojamientos
    success_url = "../alojamientos/list" 
    
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def register(request):
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST) 
        
        if form.is_valid():
            username=form.cleaned_data["username"] 
            form.save() 
            
            return render(request, "App/inicio.html", {"mensaje":f"Bienvenidooo {username} - tu usuario fue creado!!!"})
    
    else: #si la request no tenia un metodo post, se genera el userregisterform
        
        #form = UserCreationForm() - no se porq ponemos esto!!
        form= UserRegisterForm()
        
    return render(request, "App/register.html", {"form": form})


def login_request(request):
    
    if request.method=="POST": #si recibi un post de la request hago este y sino me voy al else
    
        form = AuthenticationForm(request, data = request.POST)
              
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
           
            contrasenia= form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contrasenia)
        
            if user is not None: 
                login(request, user)
                
                return render(request, "App/inicio.html", {"mensaje":f"Bienvenidooo {usuario}!!!"})
            
            else:
            
                return render(request, "App/inicio.html", {"mensaje":"Datos incorrectos, Volve a logearte!!"})
          
        else:
                   return render(request, "App/inicio.html", {"mensaje":"Formulario erroneo!!"})
    
    form = AuthenticationForm()
    
    return render (request, "App/login.html", {"form":form})


        
   
    
    
    
