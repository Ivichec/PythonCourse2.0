import findspark

findspark.init()

from pyspark import SparkContext

from pyspark.sql import SQLContext

sc = SparkContext('local', 'Spark SQL')
sqlc = SQLContext(sc)
empleados = sqlc.read.json("empleados.json")
# PASO MUY IMPORTANTE: Generamos una tabla llamada EMP con los datos del JSON.
# Al generar la tabla podemos realizar consultas SQL.
empleados.createOrReplaceTempView("EMP")
# Realizamos  consulta SQL
empleadosConsulta = sqlc.sql("SELECT Apellido, Salario FROM EMP")
print(empleadosConsulta)
panda1 = empleadosConsulta.toPandas()
panda1.plot(kind='barh', x='Apellido', y='Salario', colormap='winter_r')
