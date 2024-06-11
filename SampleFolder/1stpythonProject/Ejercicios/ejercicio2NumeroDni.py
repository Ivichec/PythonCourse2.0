numeroDni = int(input('Escribe tu numero de dni: '))
chars = ["t","r","w","a","g","m","t","y","f","p","d","x","b","n","j","z","s","q","v","h","l","c","k","e","t"]
print('Tu letra de dni es: ',chars[int(numeroDni%23)+1].upper())