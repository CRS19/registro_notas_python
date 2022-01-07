from CRUD import Crud
arreglo_estudiantes = Crud.obtener_estudiantes()
data = []
for index,estudiante in enumerate(arreglo_estudiantes):
    print(index)

