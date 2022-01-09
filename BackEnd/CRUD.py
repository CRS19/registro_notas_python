from numpy import NaN, nan
import pandas as pd
from Clase_Semilla import Estudiante

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
#print(data_Padre)
data_Hijo=data_Padre.iloc[FILA-2:NRO_DE_ESTUDIANTES+FILA-2,COLUMNA-1:24]
#print(data)




class Crud:
        
    def obtener_estudiantes():
        estudiantes = []

        for i in range(NRO_DE_ESTUDIANTES):
            nombre_apellido = data_Hijo.iat[i,NOMBRE_APELLIDO] 
            id = data_Hijo.iat[i,ID]
            cedula = data_Hijo.iat[i,CEDULA]
            registro = 0 
            estudiante = Estudiante(id, cedula, nombre_apellido, registro)
            estudiantes.append(estudiante)


        return estudiantes

    def RegistrarAsistencia(self,PosicionEstudianteLista):
        data_Hijo.iat[PosicionEstudianteLista,REGISTRO_ASISTENCIA]="X"
        print(data_Hijo)
        data_Padre.iloc[FILA-2:NRO_DE_ESTUDIANTES+FILA-2,COLUMNA-1:24]=data_Hijo
        data_Padre.to_excel(f"{DIRECCION_EXCEL}\\Prueba.xlsx",index=False)

