from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "deportes/Inicio.html")
def mensaje(request):
    return HttpResponse("<H2>Buenos Dias</H2>")
def equipo(request):
    nombre='Real Madrid'
    dato=nombre.upper()
    lista={
        "equipo1":dato
    }
    return render(request, "deportes/equipoPreferido.html",lista)