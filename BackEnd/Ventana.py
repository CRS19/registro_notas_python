from datetime import datetime
import tkinter as tk
from CRUD import Crud
crud=Crud()
#arreglo de objetos de la clase estudiantes 
arreglo_estudiantes = Crud.obtener_estudiantes()
data = []
for index,estudiante in enumerate(arreglo_estudiantes):
    data.append([index+1,estudiante.nombre_apellido, estudiante.registro])
#index es el contador
def ObtenerAsistencia():
    for i in range(len(data)):
        if ArregloDeCheckButtons[i].get()==1:
            #estoy llamando al metodo de la clase estudiante
            # al estudiante que esta en la posicion que valga ahi, registrara su asistencia (crud ayuda a guardar la asistencia) 
            arreglo_estudiantes[i].registrar_asistencia(i,crud)
    
FechaHoy=datetime.now()
fecha=datetime.strftime(FechaHoy,"%d/ %m /%Y")  

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


frame_main = tk.Frame(root, bg="white")
frame_main.grid(sticky='news')

label0 = tk.Label(frame_main, text=f"Fecha: {fecha}", fg="black")
label0.grid(row=0, column=0, pady=(5, 0), sticky='nw')

label1 = tk.Button(frame_main, text="Regresar", fg="green")
label1.grid(row=3, column=0, pady=5, sticky='nw')

label2 = tk.Button(frame_main, text="Guardar", fg="red",command=ObtenerAsistencia)
label2.grid(row=4, column=0, pady=5, sticky='ne')

#Creamos un nuevo lienzo a partir del frame main 
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
#Permite modificar el tamaño del lienzo creado
frame_canvas.grid_propagate(False)

#Creamos otro lienzo dentro de frame canvas
canvas = tk.Canvas(frame_canvas, bg="white")
canvas.grid(row=0, column=0, sticky="news")
#Sticky= Si el elemento es menor que la grilla se ubicara dentro de las posiciones nsew
#creamos nuestra scrollbar 
barra = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
barra.grid(row=0, column=1, sticky='ns')
#maneja la vista del canvas
canvas.configure(yscrollcommand=barra.set)

#Creamos otro lienzo para nuestra tabla 
frame_buttons = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

#Creamos las etiquetas de los titulos de nuestra tabla 


tk.Label(frame_buttons, text="Nr.", anchor="w", bg="green").grid(row=0, column=0, sticky="ew")
tk.Label(frame_buttons, text="Apellidos y Nombres", anchor="w",bg="green").grid(row=0, column=1, sticky="ew")
tk.Label(frame_buttons, text="Asistencia", anchor="w",bg="green").grid(row=0, column=2, sticky="ew")
tk.Label(frame_buttons, text="Action", anchor="w",bg="green").grid(row=0, column=3, sticky="ew")

def delete(nr):
    print ("deleting...nr=", nr)

ArregloDeCheckButtons=[]

#esta sacando por partes
for (posicion, nombre, registro) in data:
    posicion_label = tk.Label(frame_buttons, text=str(posicion), anchor="w", bg="white") 
    nombre_label = tk.Label(frame_buttons, text=nombre, anchor="w", bg="white")
    registro_button = tk.Button(frame_buttons, text="Delete", command=lambda nr=posicion: delete(nr))
    Val_CheckButton = tk.IntVar()
    active_cb = tk.Checkbutton(frame_buttons, onvalue=True, offvalue=False,variable=Val_CheckButton,bg="gray")
    ArregloDeCheckButtons.append(Val_CheckButton)
    if registro:
        active_cb.select()
    else:
        active_cb.deselect()

    posicion_label.grid(row=posicion, column=0, sticky="ew")
    nombre_label.grid(row=posicion, column=1, sticky="ew")
    active_cb.grid(row=posicion, column=2, sticky="ew")
    registro_button.grid(row=posicion, column=3, sticky="ew")




#Actualizar los tamaños del frame buttons
frame_buttons.update_idletasks()

#Configuramos el tamaño
first5columns_width = 380
first5rows_height = 350
frame_canvas.config(width=first5columns_width + barra.winfo_width(),
                    height=first5rows_height)

#Ubicamos el scrollbar en el lienzo que queramos
canvas.config(scrollregion=canvas.bbox("all"))


#Ejecuta el programa
root.mainloop()
