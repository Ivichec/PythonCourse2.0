from django.shortcuts import render
from Peliculas.models import Empleado1


def index(request):
    emple = Empleado1()
    condicional = emple.devolverdato()
    condicional1 = {
        'datos': condicional,
        'home': True,
        'personajes': False,
        'borrado': False
    }
    return render(request, "data/template1Index.html", condicional1)


def listarSerie(request):
    ser = request.GET['Serie']
    emple = Empleado1()
    condicional = emple.devolverserie(ser)
    condicional1 = {
        'datos': condicional,
        'home': False,
        'personajes': True,
        'borrado': False
    }
    return render(request, "data/template1Index.html", condicional1)


def insertarDato(request):
    idper = int(request.POST['idper'])
    nom = request.POST['nom']
    img = request.POST['img']
    idserie = int(request.POST['idserie'])
    Empleado1().insertdato(idper,nom,img,idserie)
    condicional = Empleado1().devolverserie(idserie)
    condicional1 = {
        'datos': condicional,
        'home': False,
        'personajes': True,
        'borrado': False
    }
    return render(request, "data/template1Index.html", condicional1)


def alta(request):
    return render(request, "data/template2Alta.html")


def Borrar(request):
    return render(request, "data/template3Baja.html")

def baja1(request):
    idserie = int(request.POST['idserie'])
    emple = Empleado1()
    baja = emple.baja(idserie)
    condicional = emple.devolverdato()
    if baja == 200:
        borrado = True
    else:
        borrado = False
    print("ñsa´kjkfdg´pawskjfgáls´çgàfs" + str(borrado))
    condicional1 = {
        'datos': condicional,
        'home': True,
        'personajes': False,
        'borrado': {'borrado1':[True],'borrado2':[borrado]}
    }
    return render(request, "data/template1Index.html", condicional1)

