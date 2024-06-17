from django.urls import path

from gestion import views

urlpatterns =[
    path('' ,views.index ,name='index'),
    path('perfil' ,views.index2 ,name='perfil')

]