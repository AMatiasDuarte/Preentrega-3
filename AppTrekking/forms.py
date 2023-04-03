from django import forms


class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=8)
    fecha_nacimiento = forms.DateField()
    
    
class EventoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100, default="Por_hacer")
    creado = forms.DateTimeField(auto_now_add=True)
    modificado = forms.DateTimeField(auto_now=True)
    
    
class TrekkingForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100, default="Por_hacer")
    creado = forms.DateTimeField(auto_now_add=True)
    modificado = forms.DateTimeField(auto_now=True)
    