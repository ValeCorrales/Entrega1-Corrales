from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),  
    path('ciudades/', views.ciudades, name="Ciudades"),
    path('restaurantes/', views.restaurantes, name="Restaurantes"),
    path('alojamientos/', views.alojamientos, name="Alojamientos"), 
    path('contactanos/', views.contactanosFormulario, name="Contactanos"), 
    #path('alojamientoFormulario/', views.alojamientoFormulario, name="AlojamientoFormulario"), 
    #path('ciudadesFormulario/', views.ciudadesFormulario, name="CiudadesFormulario"), 
    #path('restaurantesFormulario/', views.restaurantesFormulario, name="RestaurantesFormulario"), 
    
    #segunda entrega
    path('about/', views.about, name="About"), 
    
    #URLS CIUDADES
    path('ciudades/list/', views.CiudadesList.as_view(), name='CiudadesList'),
    path(r'^(?P<pk>\d+)$', views.CiudadesDetalle.as_view(), name='CiudadesDetail'), 
    path(r'^nuevo$', views.CiudadesCreacion.as_view(), name='CiudadesNew'), #esta url es para crear
    path(r'^editar/(?P<pk>\d+)$', views.CiudadesUpdate.as_view(), name='CiudadesEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CiudadesDelete.as_view(), name='CiudadesDelete'),
    
    #URLS Restaurantes
    path('restaurantes/list/', views.RestaurantesList.as_view(), name="RestaurantesList"), 
    path(r'^(?P<pk>\d+)$', views.RestaurantesDetalle.as_view(), name='RestaurantesDetail'), 
    path(r'^nuevo$', views.RestaurantesCreacion.as_view(), name='RestaurantesNew'), #esta url es para crear
    path(r'^editar/(?P<pk>\d+)$', views.RestaurantesUpdate.as_view(), name='RestaurantesEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.RestaurantesDelete.as_view(), name='RestaurantesDelete'),
    
    #URLS ALOJAMIENTOS
    path('alojamientos/list/', views.AlojamientosList.as_view(), name="AlojamientosList"), 
    path(r'^(?P<pk>\d+)$', views.AlojamientosDetalle.as_view(), name='AlojamientosDetail'), 
    path(r'^nuevo$', views.AlojamientosCreacion.as_view(), name='AlojamientosNew'), #esta url es para crear
    path(r'^editar/(?P<pk>\d+)$', views.AlojamientosUpdate.as_view(), name='AlojamientosEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.AlojamientosDelete.as_view(), name='AlojamientosDelete'),
    
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='App/logout.html'), name='Logout'),
]