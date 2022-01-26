from datetime import datetime

fechact = datetime.now()
fecha = datetime.strftime(fechact, "%d/%m/%Y")
class Estudiante:

    def __init__ (self, id, cedula, nombre_apellido, notas, asistencias):
        self.id = id
        self.cedula = cedula
        self.nombre_apellido = nombre_apellido
        self.notas = notas
        self.asistencias = asistencias


    def registrar_asistencia(self,crud):
       #crud porfavor dame registrando la asistencia del estudiante en la posicion
        self.asistencias.append({"FECHA": fecha, "ASISTENCIAS":True})
        crud.RegistrarAsistencia(self.id, self.asistencias)