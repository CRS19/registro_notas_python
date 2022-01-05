from numpy import NaN, nan
import pandas as pd
from Clase_Semilla import Estudiante

NOMBRE_APELLIDO=7
ID=1
CEDULA=3
PAGADO=16
APOYO=19


data=pd.read_excel("D:\\Documents\\UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE\\TECNOLOGIA EN SOTFWARE\\PYHTON SOTFWARE\\SEGUNDO PARCIAL\\PROYECTOO\\Prueba.xlsx",skiprows=12)
print(data)

print(data.iat[0,7])


def obtener_estudiantes():
    condicion_parada=''

    contador=0
    while type (condicion_parada)!=type(0.1):
        condicion_parada=data.iat[contador,NOMBRE_APELLIDO]
        if type (condicion_parada)!=type(0.1):
            print(condicion_parada)    
        contador=contador+1


class Crud:
    def insertarasistencia():
        data=pd.read_excel("D:\\Documents\\UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE\\TECNOLOGIA EN SOTFWARE\\PYHTON SOTFWARE\\SEGUNDO PARCIAL\\PROYECTOO\\Test.xlsx",skiprows=3)
        print(data)
        