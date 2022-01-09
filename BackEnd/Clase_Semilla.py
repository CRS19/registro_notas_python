from typing import SupportsFloat

class Estudiante:

    def __init__ (self, id, cedula, nombre_apellido, registro):
        self.id = id
        self.cedula = cedula
        self.nombre_apellido = nombre_apellido
        self.registro = registro
    
    def asistir(self,asistencia):
        
        #asistencia.upper()
        #if asistencia == "SI":
            
        #else:

        print(f"El estudiante {asistencia} asistio")

    def registrar_asistencia(self,posicion,crud):
        crud.RegistrarAsistencia(posicion)

    def nueva_asistencia(self):
        self.asistencia.append()
    
             