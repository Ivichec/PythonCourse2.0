from django.urls import path

from jugadores import views

urlpatterns = [
    path('', views.jugadores, name='jugadores'),
    path('amigos', views.amigos, name='amigos')
]
