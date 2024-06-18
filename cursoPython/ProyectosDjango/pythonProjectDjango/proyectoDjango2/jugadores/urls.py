from django.urls import path

from jugadores import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jugadores', views.jugadores, name='jugadores'),
    path('amigos', views.amigos, name='amigos'),
    path('peliculas', views.peliculas, name='peliculas')
]
