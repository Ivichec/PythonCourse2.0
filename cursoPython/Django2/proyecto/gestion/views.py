from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "Ivan/plantilla1.html")
def index2(request):
    nombre = 'Iván'
    apellido = 'Checa'
    dato = nombre.upper()
    lista = {
        "nombre": nombre,
        "apellido": apellido
    }
    return render(request, "Ivan/plantilla2.html", lista)

