import tkinter as tk
data = [
            # Nr. Name  Active
            [1,   "Alvarez", False],
            [2,   "Arias", False],
            [3,   "Aviles", False],
            [4,   "Caceres", True],
            [5,   "Caiza", False],
            [6,   "Camacho", True],
            [7,   "Chimbolema", True],
            [8,   "Coello", False],
            [9,   "Duran", True],
            [10,   "Garces", True],
            [11,   "Gavilema", False],
            [12,   "Gonzalez", True],
            [13,   "Gualotuña", True],
            [14,   "Guarnizo", False],
            [15,   "Inca Saigua Diego Fernando", True],
            [16,   "Iza", True],
            [17,   "Jimenez", False],
            [18,   "Luna", True],
            [19,   "Moncayo", True],
            [20,   "Montenegro", False],
            [21,   "Naranjo", True],
            [22,   "Osejo", True],
            [23,   "Puma", False],
            [24,   "Quero", True],
            [25,   "Quintana", True],
            [26,   "Rodriguez", False],
            [27,   "Ruiz", True],
            [28,   "Samueza", True],
            [29,   "Singo", False],
            [30,   "Suntaxi", True],
            [31,   "Tupiza", True],
            [32,   "Zambrano", False],
            [33,   "Zurita", True],
            [34,   "Ñacata", True],
            ]

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="white")
frame_main.grid(sticky='news')

label1 = tk.Button(frame_main, text="Regresar", fg="green")
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
tk.Label(frame_buttons, text="Name", anchor="w",bg="green").grid(row=0, column=1, sticky="ew")
tk.Label(frame_buttons, text="Active", anchor="w",bg="green").grid(row=0, column=2, sticky="ew")
tk.Label(frame_buttons, text="Action", anchor="w",bg="green").grid(row=0, column=3, sticky="ew")

def delete(nr):
    print ("deleting...nr=", nr)

row = 1
for (nr, name, active) in data:
    nr_label = tk.Label(frame_buttons, text=str(nr), anchor="w", bg="white")
    name_label = tk.Label(frame_buttons, text=name, anchor="w", bg="white")
    action_button = tk.Button(frame_buttons, text="Delete", command=lambda nr=nr: delete(nr))
    active_cb = tk.Checkbutton(frame_buttons, onvalue=True, offvalue=False,bg="gray")
    if active:
        active_cb.select()
    else:
        active_cb.deselect()

    nr_label.grid(row=row, column=0, sticky="ew")
    name_label.grid(row=row, column=1, sticky="ew")
    active_cb.grid(row=row, column=2, sticky="ew")
    action_button.grid(row=row, column=3, sticky="ew")

    row += 1






# Update buttons frames idle tasks to let tkinter calculate buttons sizes
frame_buttons.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
first5columns_width = 300
first5rows_height = 350
frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                    height=first5rows_height)

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
root.mainloop()
