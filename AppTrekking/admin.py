from django.contrib import admin
from AppTrekking.models import Trekking, Persona, Evento

admin.site.register(Trekking, Persona, Evento)


