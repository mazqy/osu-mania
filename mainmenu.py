import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Import Pillow for better image handling
import os
import tkinter.font as tkFont

root = tk.Tk()
root.title("Beatmap selector")
root.iconbitmap("data/mania_icon.ico")
root.geometry("500x500")

# Función para seleccionar la imagen
def seleccionar_imagen():
    global pfp
    archivo_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
    if archivo_imagen:
        try:
            img = Image.open(archivo_imagen)
            img = img.resize((75, 75), Image.Resampling.LANCZOS)  # Resize the image to fit the label
            pfp = ImageTk.PhotoImage(img)
            imagen_label.config(image=pfp)
            imagen_label.image = pfp  
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

# Crear una fuente personalizada
custom_font = tkFont.Font(family="Helvetica", size=25)
custom_font2 = tkFont.Font(family="Helvetica", size=25, weight="bold")

text = tk.Label(root, text="BEATMAP SELECTOR", font=custom_font2, foreground="blue")
text.pack()

# Ajuste del tamaño del Listbox
maplist = tk.Listbox(root, width=20, height=5, font=custom_font)
maplist.pack(pady=10)

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

beatmap_selected = ""

def on_button_click():
    global beatmap_selected
    beatmap_selected = maplist.get(maplist.curselection())
    root.destroy()

# Ajuste del tamaño del Button
button = tk.Button(root, text="PLAY", command=on_button_click, width=20, height=2)
button.pack(pady=10)

# Botón para seleccionar imagen
seleccionar_imagen_button = tk.Button(root, text="Seleccionar Imagen de perfil", command=seleccionar_imagen)
seleccionar_imagen_button.pack(pady=10)

# Etiqueta para mostrar la imagen seleccionada
imagen_label = tk.Label(root)
imagen_label.pack(pady=10)

# Etiqueta para mostrar el nombre "melis"
nombre_label = tk.Label(root, text="1# melis", font=custom_font)
nombre_label.pack()

root.mainloop()
