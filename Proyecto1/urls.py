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
from AppTrekking.views import crear_persona, crear_evento, crear_trekking
from AppTrekking.views import BuscarPersonas, BuscarEventos, BuscarTrekkings
from CommunityTrekk.views import index, PostList, PostDetail, PostCreate, PostUpdate, PostDelete
from CommunityTrekk.views import SignUp, Login, Logout, ProfileUpdate, ProfileCreate, MensajeCreate, MensajeDelete, MensajeList, ProfileList
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-template', mostrar_template),
    path('mis-trekkings/', mostrar_mis_trekkings, name="mis-trekking"),
    path('mis-personas/', mostrar_mis_personas, name="mis-persona"),
    path('mis-eventos/', mostrar_mis_eventos, name="mis-evento"),
    path('', index, name="index"),
    path('personas/create', crear_persona, name="personas-create"),
    path('trekkings/create', crear_trekking, name="trekkings-create"),
    path('eventos/create', crear_evento, name="eventos-create"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    path('eventos/list', BuscarEventos.as_view(), name="eventos-list"),
    path('trekkings/list', BuscarTrekkings.as_view(), name="trekkings-list"),
    path('post/list', PostList.as_view(), name="post-list"),
    path('post/<pk>/detail', PostDetail.as_view(), name="post-detail"),
    path('post/create', PostCreate.as_view(), name="post-create"),
    path('post/<pk>/update', PostUpdate.as_view(), name="post-update"),
    path('post/<pk>/delete', PostDelete.as_view(), name="post-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('profile/list', ProfileList.as_view(), name="profile-list"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

