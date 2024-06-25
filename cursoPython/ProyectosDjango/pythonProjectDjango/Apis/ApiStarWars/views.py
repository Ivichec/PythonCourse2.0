from django.shortcuts import render
import requests
from requests.exceptions import HTTPError


def index(request):
    global condicional
    api_url = "https://swapi.dev/api/people/"
    response = requests.get(api_url)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    condicional = {
         "datos": jsonResponse
    }
    return render(request, "directorio1/Index.html", condicional)
