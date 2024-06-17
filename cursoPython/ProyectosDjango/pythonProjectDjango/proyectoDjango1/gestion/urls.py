from django.urls import path

from gestion import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lunes', views.mensaje, name='index'),
    path('futbol', views.equipo, name='equipo')
]