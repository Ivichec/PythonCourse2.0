from django.urls import path

from graficos import views

urlpatterns = [
    path('', views.comerciales, name='comerciales')
]