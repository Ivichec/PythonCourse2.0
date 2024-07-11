import matplotlib.pyplot as plt

numeroM = int(input('Numero de productos:'))

datosP = []
datosT = []

while numeroM > 0:
    precio = int(input('Precio Producto ($):'))
    tamano = int(input('Tamaño mesa (cm):'))
    datosP.append(precio)
    datosT.append(tamano)
    numeroM = numeroM - 1

print(datosT)

# Crear el grafico de barras
plt.scatter(datosP, datosT)
#Personalizar el gráfico
plt.title('Relacion precio ($) vs Tamaño de mesas de comedor (cm)')
plt.xlabel('Precio ($)')
plt.ylabel('Tamaño (cm)')
#Salvar imagen en un fichero
plt.savefig('dispersion.png')
#Mostrar el gráfico
plt.show()
