
class Estudiante:

    def __init__ (self, id, cedula, nombre_apellido, registro):
        self.id = id
        self.cedula = cedula
        self.nombre_apellido = nombre_apellido
        self.registro = registro

#Este metodo va a registrar la asistencia en esa posicion por medio del crud (objeto)
#posicion es un numero , el self es la que hacer referencia a la clase en si misma 
    def registrar_asistencia(self,posicion,crud):
        crud.RegistrarAsistencia(posicion)
    #ayuda a registrar la asistencia
         