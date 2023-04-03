from django import forms


class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=8)
    fecha_nacimiento = forms.DateField()
    
    
class EventoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100)
    creado = forms.DateField()
    modificado = forms.DateField()
    
    
class TrekkingForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100)
    creado = forms.DateField()
    modificado = forms.DateField()
    