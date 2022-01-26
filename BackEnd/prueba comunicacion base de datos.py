from pydoc import doc
from tkinter import messagebox, ttk
from tkinter import*
from Archivo_que_maneja_el_Excel import cliente


BaseDeDatos=cliente['Proyecto']
AccederaColeccion=BaseDeDatos['NRC']
Nombres=""
def MostrarNRC():
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        i=0
        for documento in AccederaColeccion.find():
            tabla.insert('',i,text=documento["nombre"],value=documento["Cedula"])
            i+=1
            print(documento)   
def CrearRegistro():
    if len(nombre.get())!=0 and len(cedula.get())!=0:
        documento={"nombre":nombre.get(),"Cedula":cedula.get()}
        AccederaColeccion.insert_one(documento)
        nombre.delete(0,END)
        cedula.delete(0,END)
    else: 
        messagebox.showerror(message="Los campos no pueden estar vacios")
    MostrarNRC()

#def dobleClick(event):
#    global Nombres
#    Nombres=tabla.item(tabla.selection())["text"]
#    documento=AccederaColeccion.find({"nombre":Nombres})[0]
#    nombre.delete(0,END)
#    nombre.insert(0,documento["nombre"])
#    cedula.delete(0,END)
#    cedula.insert(0,documento["Cedula"])
#    boton["state"]="disabled"
#    ed["state"]="normal"
#def editarRegistro():
#    if len(nombre.get())!=0 and len(cedula.get())!=0:
#        boton["state"]="normal"
#        ed["state"]="disabled"

ventana= Tk()
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=3)
tabla.heading("#0",text="Apellidos y Nombres")
tabla.heading("#1",text="Cedula")
tabla.bind("<Double-Button-1>",dobleClick)
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
#Editar
#ed=Button(ventana,text="Editar Estudiante",command=editarRegistro,bg="yellow",fg="white")
#ed.grid(row=6,columnspan=2)
#ed["state"]="disabled"

MostrarNRC()
ventana.mainloop()
