from django.urls import path

from emp import views

urlpatterns = [
    path('', views.index, name='index')
]
