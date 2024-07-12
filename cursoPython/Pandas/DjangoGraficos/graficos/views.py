from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt, mpld3


def comerciales(request):
    # Datos
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
    ventas = [120, 85, 95, 150, 110]

    fig = plt.figure()

    plt.bar(meses, ventas)
    plt.title(f'Ventas de {meses[0]} - {meses[len(meses) - 1]}')
    plt.xlabel('Meses')
    plt.ylabel('Ventas')

    g = mpld3.fig_to_html(fig)
    return HttpResponse(g)