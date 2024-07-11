import pandas as pd
df = pd.read_csv('datos.csv', delimiter=';')
df.to_excel('Notas.xlsx', index=False)