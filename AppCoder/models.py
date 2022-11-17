from django.db import models

# Create your models here.
class Sector(models.Model):

    nombre=models.CharField(max_length=40)  
    profesion=models.CharField(max_length=40) 

    def __str__(self) -> str:
        return self.nombre+""+str(self.profesion) 

class Profesional(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Contacto(models.Model):

    telefono=models.IntegerField()
    localidad=models.CharField(max_length=40) 

