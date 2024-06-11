print("--------------LISTAS-------------")

print("ORDENANDO LISTAS ASCENDENTE")
notas= [1,10,6,7,4,9]
notas.sort()
print(notas)
print("Nota más baja:",notas[0])
print("Segunda nota más baja:",notas[1])


print("ORDENANDO LISTAS DESCENDENTE")
notas.sort(reverse=True)
print(notas)
print("Nota más alta:",notas[0]) 
print("Segunda nota más alta:",notas[1])


print("--------------LISTAS-------------")

print("ORDENANDO LISTAS ASCENDENTE")
alumnos= ["BENITO","FLORO","ALEX","ANDREA","ZAMORA"]
alumnos.sort()
print(alumnos)
print("Primer alumno de la lista:",alumnos[0])
print("Segundo alumno de la lista:",alumnos[1])


print("ORDENANDO LISTAS DESCENDENTE")
alumnos.sort(reverse=True)
print(alumnos)
print("Último alumno de la lista:",alumnos[0])
print("Penúltimo alumno más alta:",alumnos[1])