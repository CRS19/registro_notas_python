from tkinter import messagebox, ttk
from tkinter import*
from pymongo import MongoClient 

cliente=MongoClient('localhost')
BaseDeDatos=cliente['Proyecto']
Colecciones=BaseDeDatos.list_collection_names()

def CrearNRC():
    nrc=entra.get()
    if nrc in Colecciones:
        messagebox.showerror(message="Ya existe el NRC")
    else:
        NuevaColeccion=BaseDeDatos.create_collection(nrc)
        messagebox.showinfo(message="Curso Creado")






nuevaVentana=Tk()
nuevaVentana.title("Crear Curso")
nuevaVentana.geometry("300x100")

entra=Entry(nuevaVentana,width=20)
entra.grid(row=0,column=1)


enviar=Button(nuevaVentana, text="Crear NRC",command=CrearNRC,bg="green",fg="white")
enviar.grid(row=1,column=1)

nuevaVentana.mainloop()