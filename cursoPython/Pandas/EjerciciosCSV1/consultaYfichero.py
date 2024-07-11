import cx_Oracle
import pandas as pd

conexion = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

df = pd.read_sql_query('SELECT * FROM emp', conexion)

print('*** DATA FRAME EMP ***')
print(df)

df.to_excel('Emp.xlsx', index=False)