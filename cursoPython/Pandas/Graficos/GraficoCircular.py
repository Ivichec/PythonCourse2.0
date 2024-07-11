import matplotlib.pyplot as plt

#Datos
x = ['Atletico de Madrid', 'Betis', 'Barcelona', 'Real Madrid']
y =[15, 10, 15, 25]
# Crear el grafico de barras
plt.pie(y, labels=x, autopct='%1.1f%%', colors=['red', 'lightblue', 'yellow', 'purple'])
#Personalizar el gráfico
plt.title('Gráfico de Quesito',color='b')
plt.legend(x,
          title="Equipos",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
#Salvar imagen en un fichero
plt.savefig('pie.png')
#Mostrar el gráfico
plt.show()