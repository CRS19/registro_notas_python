from ReportePDF import reportePDF
from Archivo_que_maneja_el_Excel import Crear
from datetime import datetime

fechact = datetime.now()
fecha = datetime.strftime(fechact, "%d/%m/%Y")

def generarReporte(titulo, cabecera, datos, nombre_PDF):
    # llamar a la clase reportePDF para construir y exportar el PDF con los datos que le llegan
    # por parametro 


    reporte = reportePDF(titulo, cabecera, datos, nombre_PDF).Exportar()
    print(reporte)

# recibir el parametro de la fecha (fecha)
def construirDataAsitenciaParaElPdf():
    arreglo_estudiantes = Crear.obtener_estudiantes()

    cabecera = (
        ("ID", "ID"),
        ("APELLIDOS Y NOMBRES", "APELLIDOS Y NOMBRES"),
        ("ASISTENCIAS", "ASISTENCIAS"),
        )

    #datos = [{"ID": '12312', "APELLIDOS Y NOMBRES": "PEPE", "ASISTENCIA": "SI"}]

    
    datos = []
    for index, estudiante in enumerate(arreglo_estudiantes):
        datos.append({"ID": estudiante.id, "APELLIDOS Y NOMBRES": estudiante.nombre_apellido, "ASISTENCIAS": "NO"})
        for registro_fecha in estudiante.asistencias:
            # reemplazar la fecha de la libreria por la fecha ingresada por el text input
            if(registro_fecha["FECHA"] == fecha):
                datos[index]["ASISTENCIAS"] = "SI"
    

    generarReporte('Reporte Asistencia', cabecera, datos, "Reporte asistencia.pdf")

    # CREAR LA FUNCION llamada ->  construirDataNotasParaElPdf que hace lo mismo que la funcoon de arriba solo que con las notas

    # cabecera = (
    #     ("ID", "ID"),
    #     ("APELLIDOS Y NOMBRES", "APELLIDOS Y NOMBRES"),
    #     ("NOTA_PARCIAL1", "NOTA_PARCIAL1"),
    #     ("NOTA_PARCIAL2", "NOTA_PARCIAL2"),
    #     ("NOTA_PARCIAL3", "NOTA_PARCIAL3"),
    #     )

     # for estudiante in arreglo_estudiantes:
     #    datos.append({"ID": estudiante.id, "APELLIDOS Y NOMBRES": estudiante.nombre_apellido, "NOTA_PARCIAL1": estudiante.notas["NOTA_PARCIAL1"],})