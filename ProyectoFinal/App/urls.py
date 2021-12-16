from django.urls import path
from App import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),  
    path('ciudades/', views.ciudades, name="Ciudades"),
    path('restaurantes/', views.restaurantes, name="Restaurantes"),
    path('alojamientos/', views.alojamientos, name="Alojamientos"), 
    path('contactanos/', views.contactanosFormulario, name="Contactanos"), 
    path('alojamientoFormulario/', views.alojamientoFormulario, name="AlojamientoFormulario"), 
    path('ciudadesFormulario/', views.ciudadesFormulario, name="CiudadesFormulario"), 
    path('restaurantesFormulario/', views.restaurantesFormulario, name="RestaurantesFormulario"), 
    
]