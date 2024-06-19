from django.urls import path

from peliculas import views

urlpatterns = [
    path('', views.index, name='index')
]
