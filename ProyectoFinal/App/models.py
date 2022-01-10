from django.db import models

# Create your models here.

class Ciudades(models.Model):
    
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    continente = models.CharField(max_length=40)
    calificacion = models.IntegerField()
    
    def __str__(self) -> str:
        return f"CIUDAD {self.nombre}, PAIS: {self.pais}, CONTINENTE: {self.continente}, CALIFICACION {self.calificacion}"
    
class Restaurantes(models.Model):
    
    nombre = models.CharField(max_length=40)
    tipoDeComida = models.CharField(max_length=40)
    calificacion = models.IntegerField()
    
    def __str__(self) -> str:
        return f"RESTAURANTE {self.nombre}, TIPO DE COMIDA: {self.tipoDeComida}, CALIFICACION {self.calificacion}"
    
class Alojamientos(models.Model):
    
    nombre = models.CharField(max_length=40)
    tipoDeAlojamiento = models.CharField(max_length=40)
    calificacion = models.IntegerField()
    
    def __str__(self) -> str:
        return f"ALOJAMIENTO {self.nombre}, TIPO DE ALOJAMIENTO: {self.tipoDeAlojamiento}, CALIFICACION {self.calificacion}"
    
    
class Comentario(models.Model):
    
    nombreYApellido = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    numeroDeTelefono = models.IntegerField()
    

    
