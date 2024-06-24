from django.urls import path

from metodoget import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formularioGet', views.alta1, name='formularioGet'),
]