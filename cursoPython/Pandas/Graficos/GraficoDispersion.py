import matplotlib.pyplot as plt

#Datos
x = ['Atletico de Madrid', 'Betis', 'Barcelona', 'Real Madrid']
y =[15, 10, 15, 25]
# Crear el grafico de barras
plt.scatter(x, y)
#Personalizar el gráfico
plt.title('Gráfico de dispersion')
plt.xlabel('Equipos')
plt.ylabel('Valor en el mercade')
#Salvar imagen en un fichero
plt.savefig('dispersion.png')
#Mostrar el gráfico
plt.show()