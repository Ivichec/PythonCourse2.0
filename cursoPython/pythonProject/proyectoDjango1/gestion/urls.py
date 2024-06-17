from django.urls import path

from gestion import views

urlpatterns = [
    path('pagina1', views.index, name='index'),
    path('lunes', views.mensaje, name='index')
]