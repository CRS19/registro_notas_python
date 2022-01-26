from tkinter import messagebox, ttk
from tkinter import*
from Archivo_que_maneja_el_Excel import cliente
import tkinter as tk
from Archivo_que_maneja_el_Excel import Crear
from Generar_PDF import construirDataAsitenciaParaElPdf
objeto=Crear()

rota=Tk()
rota.title("Union") 
rota.geometry("300x100")
BaseDeDatos=cliente['Proyecto']
AccederaColeccion=BaseDeDatos['NRC']
def Enviar():
    def MostrarNRC():
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        i=0
        for documento in AccederaColeccion.find():
            tabla.insert('',i,text=documento["nombre"],value=documento["Cedula"])
            i+=1

    def CrearRegistro():
        if len(nombre.get())!=0 and len(cedula.get())!=0:
            documento={"nombre":nombre.get(),"Cedula":cedula.get()}
            AccederaColeccion.insert_one(documento)
            nombre.delete(0,END)
            cedula.delete(0,END)
        else: 
            messagebox.showerror(message="Los campos no pueden estar vacios")
        MostrarNRC()

    ventana= Tk()
    tabla=ttk.Treeview(ventana,columns=2)
    tabla.grid(row=1,column=0,columnspan=3)
    tabla.heading("#0",text="Apellidos y Nombres")
    tabla.heading("#1",text="Cedula")

    #Nombres
    Label(ventana,text="Apellidos y Nombres").grid(row=2,column=0)
    nombre=Entry(ventana)
    nombre.grid(row=2,column=1)
    #Cedula
    Label(ventana,text="Cedula").grid(row=3,column=0)
    cedula=Entry(ventana)
    cedula.grid(row=3,column=1)
    #Ingreso
    boton=Button(ventana,text="Ingresar Estudiante",command=CrearRegistro,bg="green",fg="white")
    boton.grid(row=5,columnspan=2)

    MostrarNRC()
    tabla.mainloop()

def Lavidaesunasola():
    #arreglo de objetos de la clase estudiantes 
    arreglo_estudiantes = Crear.obtener_estudiantes()
    #Crear.ComunicacionConlaBaseDeDatos
    data = []
    for index,estudiante in enumerate(arreglo_estudiantes):
        data.append([index+1,estudiante.nombre_apellido, 0])
    
    def ObtenerAsistencia():
        for i in range(len(data)):
            if ArregloDeCheckButtons[i].get()==1:
                print("ingresado")
                #estoy llamando al metodo de la clase estudiante
                # al estudiante que esta en la posicion que valga ahi, registrara su asistencia (crud ayuda a guardar la asistencia) 
                arreglo_estudiantes[i].registrar_asistencia(objeto)
    

    root = tk.Tk()
    root.grid_rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)


    frame_main = tk.Frame(root, bg="white")
    frame_main.grid(sticky='news')

    #label0 = tk.Label(frame_main, text=f"Fecha: {fecha}", fg="black")
    #label0.grid(row=0, column=0, pady=(5, 0), sticky='nw')

    label1 = tk.Button(frame_main, text="Generar PDF", fg="green",command=construirDataAsitenciaParaElPdf)
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
        Val_CheckButton = tk.IntVar(root)
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
    root.mainloop()

entrada=Entry(rota,width=20)
entrada.grid(row=0)

enviar=Button(rota, text="Ingresar",command=Enviar).grid(row=1)
otroenviar=Button(rota, text="Meabreotra",command=Lavidaesunasola).grid(row=2)


rota.mainloop()