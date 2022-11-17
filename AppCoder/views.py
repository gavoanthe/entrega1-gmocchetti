from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import views
from django.template import loader
from AppCoder.models import Contacto, Profesional, Sector
from AppCoder.forms import ContactoFormulario, ProfesionalFormulario, SectorFormulario



def sectores(self):
    plantilla = loader.get_template('AppCoder/sectores.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def profesionales(self):
    plantilla = loader.get_template('AppCoder/profesionales.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def turnos(self):
    plantilla = loader.get_template('AppCoder/turno.html')
    documento = plantilla.render()
    return HttpResponse(documento)



def inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def sectoresFormulario(request):


    if request.method == 'POST':

        miFormulario = SectorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data


        nombre = informacion['nombre']
        profesion = informacion['profesion']

        sector = Sector(nombre=nombre, profesion=profesion)
        sector.save()

        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = SectorFormulario()
        
    return render(request, 'AppCoder/sectoresFormulario.html', {'miFormulario':miFormulario})


def busquedaSector(request):
    return render(request, 'AppCoder/busquedaSector.html')


def buscar(request):

    if request.GET["sector"]:
        sector= request.GET['sector']
        sectores = Sector.objects.filter(nombre=sector)
        return render(request, 'AppCoder/resultadosBusqueda.html' , {'sector': sector,'sectores':sectores})
    else:
        respuesta = "No se ingreso ningun sector existente"
        return HttpResponse(respuesta)



def contactoFormulario(request):

    if request.method == 'POST':

        miFormulario = ContactoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            contactos = Contacto(telefono=informacion['telefono'] , localidad=informacion['localidad'])

            contactos.save()

            return render(request , "AppCoder/inicio.html")
    else:

        miFormulario = ContactoFormulario()
    return render(request , "AppCoder/contactoFormulario.html" , {"miFormulario":miFormulario})



def buscarContacto(request):

    if request.GET["localidad"]:
        localidad= request.GET['localidad']
        localidades = Contacto.objects.filter(localidad=localidad)
        return render(request, 'AppCoder/resultadoBusquedaContacto.html' , {'localidad': localidad,'localidades':localidades})
    else:
        respuesta = "No se ingreso ningun sector existente"
        return HttpResponse(respuesta)



def profesionalFormulario(request):

    if request.method == 'POST':

        miFormulario = ProfesionalFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesionales = Profesional(nombre=informacion['nombre'] , apellido=informacion['apellido'] , email=informacion['email'])

            profesionales.save()

            return render(request , "AppCoder/inicio.html")
    else:

        miFormulario = ProfesionalFormulario()
    return render(request , "AppCoder/profesionalFormulario.html" , {"miFormulario":miFormulario})



def buscarProfesional(request):

    if request.GET["nombre"]:
        nombre= request.GET['nombre']
        nombres = Profesional.objects.filter(nombre=nombre)
        return render(request, 'AppCoder/resultadoBusquedaProfesional.html' , {'nombre': nombre,'nombres':nombres})
    else:
        respuesta = "No se ingreso ningun sector existente"
        return HttpResponse(respuesta)


