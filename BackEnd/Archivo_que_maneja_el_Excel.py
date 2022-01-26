
import pandas as pd
from Clase_Estudiante import Estudiante
from pymongo import MongoClient 

NOMBRE_APELLIDO=6
ID=0
CEDULA=2
PAGADO=15
APOYO=18
REGISTRO_ASISTENCIA=21
#POR FAVOR CAMBIAR ESTA DIRECCION POR LA DIRECCION EN LA QUE USTEDES TIENEN EL ARCHIVO ECXEL, SINO NO FUNCIONA
DIRECCION_EXCEL="C:\\Users\\Usuario\\Desktop\\p2p\\proyecto\\registro_notas_python\\BackEnd"
#TO DO obtener la fila y la columna y los numeros de estudiantes desde el front y agregarlos al constructor
FILA=14
COLUMNA=2
NRO_DE_ESTUDIANTES=34

data_Padre=pd.read_excel(f"{DIRECCION_EXCEL}\\Prueba.xlsx")
#[12:46,1:24]
#iloc saca un bloque entero del frame 
data_Hijo=data_Padre.iloc[FILA-2:NRO_DE_ESTUDIANTES+FILA-2,COLUMNA-1:24]
#print(data)

cliente=MongoClient('localhost')
BaseDeDatos=cliente['Proyecto']
AccederaColeccion=BaseDeDatos['NRC']

class Crear:
        
    def obtener_estudiantes():
        estudiantes = []
        for documento in AccederaColeccion.find():
            nombre_apellido = documento["nombre"] 
            id = documento["ID"]
            cedula = documento["Cedula"]
            notas = documento["NOTAS"]
            asistencias = documento["ASISTENCIAS"]
            estudiante = Estudiante(id, cedula, nombre_apellido, notas, asistencias)
            estudiantes.append(estudiante)
        return estudiantes

    def RegistrarAsistencia(self,ID_Estudiante, ASISTENCIAS_Estudiante):
        AccederaColeccion.update_one({"ID":ID_Estudiante}, {"$set":{"ASISTENCIAS":ASISTENCIAS_Estudiante}})

    #def ComunicacionConlaBaseDeDatos(self):

        #for i in range(NRO_DE_ESTUDIANTES):
            #nombre_apellido = data_Hijo.iat[i,NOMBRE_APELLIDO] 
            #id = data_Hijo.iat[i,ID]
            #cedula = data_Hijo.iat[i,CEDULA]
            #print(AccederaColeccion.insert_one({'ID':id,'Cedula':cedula,'nombre':nombre_apellido,'NOTAS':{},'ASISTENCIAS':[]}))


        #for AlumnosDatos in AccederaColeccion.find():
            #print(AlumnosDatos["nombre"])
            
