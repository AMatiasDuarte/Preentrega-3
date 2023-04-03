from django.shortcuts import render
from AppTrekking.models import Trekking, Persona, Evento
from AppTrekking.forms import TrekkingForm, PersonaForm, EventoForm


def mostrar_template(request):
    return render(request, "AppTrekking/index.html")

def mostrar_mis_trekkings(request):
    trekkings = Trekking.objects.all()
    context= {"trekkings": trekkings, "form": TrekkingForm(),}
    return render(request, "AppTrekking/trekkings.html", context)
    
def mostrar_mis_personas(request):
    personas = Persona.objects.all()
    context= {"personas": personas, "form": PersonaForm(),}
    return render(request, "AppTrekking/personas.html", context)

def mostrar_mis_eventos(request):
    eventos = Evento.objects.all()
    context= {"eventos": eventos, "form": EventoForm(),}
    return render(request, "AppTrekking/eventos.html", context)


def crear_persona(request):
    fp= PersonaForm(request.POST)
    personas= Persona.objects.all() 
    context= {"personas": personas, "form": fp,}
    
    if fp.is_valid():
        Persona(fp.data["nombre"], fp.data["apellido"], fp.data["dni"], fp.data["fecha_nacimiento"]).save()
        
    return render(request, "AppTrekking/personas.html", context)

def crear_trekking(request):
    ft= TrekkingForm(request.POST)
    trekkings = Trekking.objects.all()
    context= {"trekkings": trekkings, "form": ft,}
    
    if ft.is_valid():
        Trekking(ft.data["nombre"], ft.data["estado"], ft.data["creado"], ft.data["modificado"]).save()
        
    return render(request, "AppTrekking/trekkings.html", context)

def crear_evento(request):
    fe= EventoForm(request.POST)
    eventos = Evento.objects.all()
    context= {"eventos": eventos, "form": fe,}
    
    if fe.is_valid():
        Evento(fe.data["nombre"], fe.data["estado"], fe.data["creado"], fe.data["modificado"]).save()
        
    return render(request, "AppTrekking/eventos.html", context)


    
    