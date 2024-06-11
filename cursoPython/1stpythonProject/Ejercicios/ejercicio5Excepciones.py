colores=dict()
colores = {"Amarillo" : "Yellow", "Rosa" : "Pink", "Azul" : "Blue", "Rojo" : "Red"}

try:
    print(colores["fff"])
except KeyError:
    print("Error con ese dato")
