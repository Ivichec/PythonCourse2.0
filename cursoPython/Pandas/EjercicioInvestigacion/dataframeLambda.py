import pandas as pd

datos = {'Nombre': ['Juan', 'Maria', 'Pedro', 'Ana'],
         'Edad': [25, 30, 35, 28],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}

df = pd.DataFrame(datos)

print('*** DATA FRAME ORIGINAL ***')
print(df)

datos['Ciudad_Mayuscula'] = list(map(lambda x: x.upper(), datos['Ciudad']))

df = pd.DataFrame(datos)

print('*** DATA FRAME datos['+"'Ciudad_Mayuscula'"+'] ***')
print(df)