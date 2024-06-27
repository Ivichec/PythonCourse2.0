import requests
import json
import cx_Oracle


class Empleado1:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insertdato(self, idper, nombre, img, idserie):
        apiurl = "https://apiseriespersonajes.azurewebsites.net/api/Personajes"
        departamento = {"idPersonaje": idper, "nombre": nombre, "imagen": img, "idSerie": idserie}
        response = requests.post(apiurl, json=departamento)
        print(departamento)
        print("Status: " + str(response.status_code))

    def baja(self, idserie):
        import requests
        apiurl = "https://apiseriespersonajes.azurewebsites.net/api/Series/"+str(idserie)
        response = requests.delete(apiurl)
        print("ñksa´jgásfkjg´ças`ñlfkg+a`sfg" + str(response.status_code))
        return str(response.status_code)

    def modificar(self, dept_no, loc):
        cursor = self.connection.cursor()
        try:
            consulta = "UPDATE DEPT SET LOC = :p1 WHERE DEPT_NO = :p2"
            cursor.execute(consulta, (loc, dept_no))
            self.connection.commit()
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
        finally:
            cursor.close()

    def devolverdato(self):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series"
        response = requests.get(api_url)
        series = response.json()
        return series

    def devolverserie(self, serie):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series/PersonajesSerie/" + str(serie)
        response = requests.get(api_url)
        series = response.json()
        return series
