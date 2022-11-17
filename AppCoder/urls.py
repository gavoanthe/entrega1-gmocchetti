from django.urls import path
from AppCoder import views


urlpatterns = [
    path('Sectores', views.sectores, name ="Sectores"),
    path('Profesionales' , views.profesionales, name ="Profesionales" ),
    path('Turno' , views.turnos, name ="Turno"),
    path('', views.inicio, name ="Inicio"),
    path('sectoresFormularios', views.sectoresFormulario, name="sectoresFormulario"),
    path('busquedaSector', views.busquedaSector, name='busquedaSector'),
    path('buscar' , views.buscar, name="buscar"),
    path('contactoFormulario' , views.contactoFormulario, name = 'contactoFormulario'),
    path('buscarContacto' , views.buscarContacto , name ="buscarContacto"),
    path('profesionaFormulario', views.profesionalFormulario , name = "profesionalFormulario"),
    path('buscarProfesional ', views.buscarProfesional, name="buscarProfesional"),

]
