import cx_Oracle


class Empleado:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        self.cursor = self.connection.cursor()

    def buscar(self, num):
        sal = self.cursor.var(cx_Oracle.NUMBER)
        comi = self.cursor.var(cx_Oracle.NUMBER)
        args = (sal, comi, num)
        self.cursor.callproc('ejercicioEmp.buscar', args)
        return [sal.getvalue(), comi.getvalue()]

    def modificar(self, sal, comi, num):
        try:
            afectados = self.cursor.var(cx_Oracle.NUMBER)
            self.cursor.callproc('ejercicioEmp.modificar', (sal, comi, num, afectados))
            return [afectados.getvalue()]
        except self.connection.Error as error:
            print("Error: ", error)
