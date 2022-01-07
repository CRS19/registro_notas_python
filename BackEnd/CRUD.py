from numpy import NaN, nan
import pandas as pd
from Clase_Semilla import Estudiante

NOMBRE_APELLIDO=7
ID=1
CEDULA=3
PAGADO=16
APOYO=19
#POR FAVOR CAMBIAR ESTA DIRECCION POR LA DIRECCION EN LA QUE USTEDES TIENEN EL ARCHIVO ECXEL, SINO NO FUNCIONA
DIRECCION_EXCEL="C:\\Users\\Usuario\\Desktop\\p2p\\proyecto\\registro_notas_python\\BackEnd"

data=pd.read_excel(f"{DIRECCION_EXCEL}\\Prueba.xlsx",skiprows=12)
#print(data)

#print(data.iat[0,7])



class Crud:
    def insertarasistencia():
        data=pd.read_excel("D:\\Documents\\UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE\\TECNOLOGIA EN SOTFWARE\\PYHTON SOTFWARE\\SEGUNDO PARCIAL\\PROYECTOO\\Test.xlsx",skiprows=3)
        print(data)
        
    def obtener_estudiantes():
        condicion_parada=''
        estudiantes = []

        contador=0
        while type (condicion_parada)!=type(0.1):   
            condicion_parada=data.iat[contador+1,NOMBRE_APELLIDO]
            nombre_apellido = data.iat[contador,NOMBRE_APELLIDO] 
            id = data.iat[contador,ID]
            cedula = data.iat[contador,CEDULA]
            registro = 0 
            estudiante = Estudiante(id, cedula, nombre_apellido, registro)
            estudiantes.append(estudiante)

            #if type (condicion_parada)!=type(0.1):
                #print(condicion_parada)    
            contador=contador+1

        return estudiantes