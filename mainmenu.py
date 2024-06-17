import customtkinter as ctk
from tkinter import filedialog, Listbox, Button, FLAT
from PIL import Image, ImageTk
import os
import tkinter.font as tkFont
from CTkListbox import *

# Función para seleccionar la imagen
def seleccionar_imagen():
    global pfp
    archivo_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
    if archivo_imagen:
        try:
            img = Image.open(archivo_imagen)
            img = img.resize((75, 75), Image.Resampling.LANCZOS)
            pfp = ImageTk.PhotoImage(img)
            imagen_label.configure(image=pfp)
            imagen_label.image = pfp  
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

# Crear la ventana principal
ctk.set_appearance_mode("System")  # Modos: "System" (predeterminado), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (predeterminado), "green", "dark-blue"

root = ctk.CTk()
root.title("osu! mania lite - Beatmap selector")
root.iconbitmap("data/mania_icon.ico")
root.geometry("750x550")
root.resizable(False, False)
# Crear una fuente personalizada
custom_font = ctk.CTkFont(family="Helvetica", size=25)
custom_font2 = ctk.CTkFont(family="Helvetica", size=25, weight="bold")
custom_font3 = ctk.CTkFont(family="Helvetica", size=25, weight="bold")
custom_font4 = ctk.CTkFont(family="Helvetica", size=40, weight="bold")

# Etiqueta de título
text = ctk.CTkLabel(root, text="BEATMAP SELECTOR", font=custom_font2, text_color="white")
text.pack(pady=15)

# Ajuste del tamaño del Listbox
maplist = CTkListbox(root)
maplist.pack(fill="both", expand=True, padx=10, pady=10)

carpetas = []

# Función para listar las carpetas
def listar_carpetas(ruta):
    global carpetas

    try:
        carpetas = [nombre for nombre in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, nombre))]
        if carpetas:
            for carpeta in carpetas:
                maplist.insert(ctk.END, carpeta)
    except Exception as e:
        print(f"Error al intentar listar carpetas: {e}")

ruta_carpeta = "beatmaps"
listar_carpetas(ruta_carpeta)

beatmap_selected = ""

# Función para manejar el clic del botón
def on_button_click():
    global beatmap_selected
    beatmap_selected = maplist.get(maplist.curselection())
    root.destroy()

# Botón para seleccionar el beatmap
button = ctk.CTkButton(root, text="PLAY", command=on_button_click, width=200, height=40)
button.pack(pady=10)

# Botón para seleccionar la imagen de perfil


centro_frame = ctk.CTkFrame(root)
centro_frame.pack(pady=10)

bg_color = centro_frame.cget("fg_color")

# Crear el botón invisible pero con texto visible
imagen_label = Button(
    centro_frame,
    text="",  # Sin texto
    command=seleccionar_imagen,
    borderwidth=0,  # Sin borde
    highlightthickness=0,
    relief=FLAT  # Sin realce
)
imagen_label.pack(side="left")

nombre_label = ctk.CTkLabel(centro_frame, text="melis", font=custom_font3)
nombre_label.pack(side="left", padx=10)

img = Image.open("data/player_data/def_img.jpg")
img = img.resize((75, 75), Image.Resampling.LANCZOS)
pfp = ImageTk.PhotoImage(img)
imagen_label.configure(image=pfp)
imagen_label.image = pfp

root.mainloop()
