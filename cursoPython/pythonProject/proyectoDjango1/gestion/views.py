from django.http import HttpResponse


def index(request):
    return HttpResponse("<H2>Página de inicio</H2>")
def mensaje(request):
    return HttpResponse("<H2>Buenos Dias</H2>")