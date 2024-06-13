import tkinter as tk
import os

root = tk.Tk()
root.title("Beatmap selector")
root.iconbitmap("data/mania_icon.ico")

maplist = tk.Listbox(root)
maplist.pack()

carpetas = []

def listar_carpetas(ruta):
    global carpetas
    if not os.path.isdir(ruta):
        print(f"La ruta {ruta} no es un directorio válido.")
        return

    try:
        carpetas = [nombre for nombre in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, nombre))]
        if carpetas:
            for carpeta in carpetas:
                print(carpeta)
        else:
            print(f"No se encontraron carpetas en {ruta}.")
    except Exception as e:
        print(f"Error al intentar listar carpetas: {e}")

ruta_carpeta = "beatmaps"
listar_carpetas(ruta_carpeta)

for carpeta in carpetas:
    maplist.insert(tk.END, carpeta)

beatmap_selected =""

def on_button_click():
	global beatmap_selected
	beatmap_selected = maplist.get(maplist.curselection())
	root.destroy()

button = tk.Button(root, text="play", command=on_button_click)
button.pack()
root.mainloop()
