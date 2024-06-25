from django.urls import path
from ApiStarWars import views

urlpatterns = [
    path('', views.index, name='index'),
]