import tkinter as tk
from turtle import width
from CRUD import Crud
crud=Crud()
arreglo_estudiantes = Crud.obtener_estudiantes()
data = []
for index,estudiante in enumerate(arreglo_estudiantes):
    data.append([index+1,estudiante.nombre_apellido, estudiante.registro])



def ObtenerAsistencia():
    for i in range(len(data)):
        if ArregloDeCheckButtons[i].get()==1:
            print(data[i][1])
            arreglo_estudiantes[i].registrar_asistencia(i,crud)

def regresar():
    root.withdraw()
    ventana = tk.Toplevel()
    ventana.geometry('400x500')
       



root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="white")
frame_main.grid(sticky='news')

label1 = tk.Button(frame_main, text="Regresar", fg="green",command=regresar)
label1.grid(row=3, column=0, pady=5, sticky='nw')

label2 = tk.Button(frame_main, text="Guardar", fg="red")
label2.grid(row=4, column=0, pady=5, sticky='nw')

# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="white")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

# Add 9-by-5 buttons to the frame


tk.Label(frame_buttons, text="Nr.", anchor="w", bg="green").grid(row=0, column=0, sticky="ew")
tk.Label(frame_buttons, text="Apellidos y Nombres", anchor="w",bg="green").grid(row=0, column=1, sticky="ew")
tk.Label(frame_buttons, text="Parcial 1", anchor="w",bg="green").grid(row=0, column=2, sticky="ew")
tk.Label(frame_buttons, text="Parcial 2", anchor="w",bg="green").grid(row=0, column=3, sticky="ew")
tk.Label(frame_buttons, text="Parcial 3", anchor="w",bg="green").grid(row=0, column=4, sticky="ew")

def delete(nr):
    print ("deleting...nr=", nr)

row = 1
ArregloDeCheckButtons=[]

for (nr, name, active) in data:
    nr_label = tk.Label(frame_buttons, text=str(nr), anchor="w", bg="white")
    name_label = tk.Label(frame_buttons, text=name, anchor="w", bg="white")
    action_button = tk.Entry(frame_buttons)
    Val_CheckButton = tk.IntVar()
    active_cb = tk.Entry(frame_buttons,bg="gray")
    ArregloDeCheckButtons.append(Val_CheckButton)
    entry_p3 = tk.Entry(frame_buttons,width=10,bg="gray")
    entry_p3.grid(row=row, column=4)
    

    nr_label.grid(row=row, column=0, sticky="ew")
    name_label.grid(row=row, column=1, sticky="ew")
    active_cb.grid(row=row, column=2, sticky="ew")
    action_button.grid(row=row, column=3, sticky="ew")

    row += 1

#print(ArregloDeCheckButtons[0].get())





# Update buttons frames idle tasks to let tkinter calculate buttons sizes
frame_buttons.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
first5columns_width = 600
first5rows_height = 350
frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                    height=first5rows_height)

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
root.mainloop()