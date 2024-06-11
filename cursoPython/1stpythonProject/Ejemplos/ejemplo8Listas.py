print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito","Floro","Alex","Andrea","Rosa","Sara"]
nombre.append("Pepito")
nombre.insert(3,"Iván")
nombre.remove("Andrea")
del nombre[0:4]   #Borra el rango de numeros que le ponemos
#del nombre[1:]   #Borra toda la lista a partir del primer valor
#del nombre[:]   #Borra toda la lista
print(len(nombre))
print(nombre) #Mostramos la cadena con todos los valores de la lista
print("Rosa" in nombre)
print("Iván" in nombre)
#print("Nombre 7:",nombre[6])