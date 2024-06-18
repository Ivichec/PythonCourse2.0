from django.http import HttpResponse
from django.shortcuts import render

def jugadores(request):
    listajugadores = [
        {
            "Nombre": "Sergio Ramos",
            "Demarcacion": "Defensa",
            "Numero": 5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero": 7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero": 9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero": 8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]
    contexto = {
        'listado_jugadores': listajugadores
    }
    return render(request, "deportes/jugadores.html", contexto)

