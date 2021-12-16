from django.shortcuts import render
from django.http import HttpResponse
from App.models import Ciudades, Restaurantes, Alojamientos, Comentario
from App.forms import AlojamientoFormulario, RestaurantesFormulario, CiudadesFormulario, ContactanosFormulario


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

def alojamientoFormulario(request):
    
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
    
    
def ciudadesFormulario(request):
    
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
 
    
def restaurantesFormulario(request):
    

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
    

        
        
   
    
    
    
