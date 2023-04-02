from django.shortcuts import render
from AppTrekking.models import Trekking, Persona, Evento

def mostrar_template(request):
    return render(request, "AppTrekking/index.html")

def mostrar_mis_trekkings(request):
    trekkings = Trekking.objects.all()
    return render(request, "AppTrekking/trekkings.html", {"trekkings" : trekkings})
    
def mostrar_mis_personas(request):
    personas = Persona.objects.all()
    return render(request, "AppTrekking/personas.html", {"personas" : personas})

def mostrar_mis_eventos(request):
    eventos = Evento.objects.all()
    return render(request, "AppTrekking/eventos.html", {"eventos" : eventos})