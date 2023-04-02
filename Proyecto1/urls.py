"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppTrekking.views import mostrar_template, mostrar_mis_trekkings, mostrar_mis_personas, mostrar_mis_eventos
from CommunityTrekk.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-template', mostrar_template),
    path('mis-trekkings/', mostrar_mis_trekkings, name="mis-trekking"),
    path('mis-personas/', mostrar_mis_personas, name="mis-persona"),
    path('mis-eventos/', mostrar_mis_eventos, name="mis-evento"),
    path('', index),   
]
