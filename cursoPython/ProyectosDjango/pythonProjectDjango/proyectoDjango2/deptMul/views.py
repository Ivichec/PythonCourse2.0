from django.shortcuts import render

# Create your views here.
from deptMul.models import Formulario


def index(request):
    return render(request, "formulario/template1Index.html")


def alta1(request):
    ofi = request.GET['Oficio']
    emple = Formulario()
    condicional = emple.insertdato(ofi)
    context = {
        'condicional1': condicional
    }
    return render(request, "formulario/formulario.html", context)
