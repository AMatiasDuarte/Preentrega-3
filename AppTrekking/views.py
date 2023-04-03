from django.shortcuts import render
from django.http import HttpResponse
from AppTrekking.models import Trekking, Persona, Evento
from AppTrekking.forms import TrekkingForm, PersonaForm, EventoForm


def mostrar_template(request):
    return render(request, "AppTrekking/index.html")

def mostrar_mis_trekkings(request):
    trekkings = Trekking.objects.all()
    context= {"trekkings": trekkings, "form": TrekkingForm()}
    return render(request, "AppTrekking/trekkings.html", context)
    
def mostrar_mis_personas(request):
    personas = Persona.objects.all()
    context= {"personas": personas, "form": PersonaForm()}
    return render(request, "AppTrekking/personas.html", context)

def mostrar_mis_eventos(request):
    eventos = Evento.objects.all()
    context= {"eventos": eventos, "form": EventoForm()}
    return render(request, "AppTrekking/eventos.html", context)


def crear_persona(request):
    fp= PersonaForm(request.POST)
    personas= Persona.objects.all() 
    context= {"personas": personas, "form": fp}
    
    if fp.is_valid():
        Persona(nombre= fp.data["nombre"], apellido= fp.data["apellido"], dni= fp.data["dni"], fecha_nacimiento= fp.data["fecha_nacimiento"]).save()
        
    return render(request, "AppTrekking/personas.html", context)

def crear_trekking(request):
    ft= TrekkingForm(request.POST)
    trekkings = Trekking.objects.all()
    context= {"trekkings": trekkings, "form": ft}
    
    if ft.is_valid():
        Trekking(nombre= ft.data["nombre"], estado= ft.data["estado"], creado= ft.data["creado"], modificado= ft.data["modificado"]).save()
        
    return render(request, "AppTrekking/trekkings.html", context)

def crear_evento(request):
    fe= EventoForm(request.POST)
    eventos = Evento.objects.all()
    context= {"eventos": eventos, "form": fe}
    
    if fe.is_valid():
        Evento(nombre= fe.data["nombre"], estado= fe.data["estado"], creado= fe.data["creado"], modificado= fe.data["modificado"]).save()
        
    return render(request, "AppTrekking/eventos.html", context)


    
    