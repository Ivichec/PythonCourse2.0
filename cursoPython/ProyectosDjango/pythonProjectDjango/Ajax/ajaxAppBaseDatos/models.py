import cx_Oracle


class Datos:
    def __init__(self):
        try:
            self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        except cx_Oracle.DatabaseError as e:
            print(f"Error connecting to database: {e}")
            self.connection = None

    def _fetch_all(self, query):
        if not self.connection:
            print("No database connection.")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            data = cursor.fetchall()
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            data = None
        finally:
            cursor.close()

        return data

    def hospital(self):
        return self._fetch_all("SELECT * FROM hospital")

    def doctores(self):
        return self._fetch_all("SELECT * FROM doctor")

    def plantilla(self):
        return self._fetch_all("SELECT * FROM plantilla")

    def close(self):
        if self.connection:
            self.connection.close()
