from django.urls import path

from formulario import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formularioPost', views.alta1, name='formularioPost'),
]