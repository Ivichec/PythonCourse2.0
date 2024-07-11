import matplotlib.pyplot as plt

#Datos
x = ['Atletico de Madrid', 'Betis', 'Barcelona', 'Real Madrid']
y =[15, 10, 15, 25]
# Crear el grafico de barras
plt.plot(x, y)
#Personalizar el gráfico
plt.title('Gráfico de Linea')
plt.xlabel('Equipos')
plt.ylabel('Valor en el mercado')
#Salvar imagen en un fichero
plt.savefig('lineal.png')
#Mostrar el gráfico
plt.show()