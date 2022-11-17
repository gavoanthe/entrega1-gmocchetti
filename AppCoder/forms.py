from django import forms

class SectorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)  
    profesion=forms.CharField(max_length=40)


class ContactoFormulario(forms.Form):
    telefono=forms.IntegerField()
    localidad=forms.CharField(max_length=40)

class ProfesionalFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()