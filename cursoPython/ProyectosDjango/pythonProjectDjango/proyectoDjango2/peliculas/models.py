from django.db import models

# Create your models here.
import cx_Oracle


class Peliculas:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def devolverdatos(self):
        cursor = self.connection.cursor()
        dato = ''
        try:
            cursor.execute("select TITULO,FOTO from peliculas")
        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
