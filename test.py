
from tkinter import filedialog as FileDialog
from tkinter import *

ventana = Tk()
ventana.title("AUGUS IDE")
ventana.geometry('800x600')

ruta = ''

#Menu
menubar = Menu(ventana)

#Logica de Archivo
def nuevo():
    mensaje.set('Nuevo fichero')
    texto.delete(1.0, END)

def abrir():
    mensaje.set('Nuevo fichero')

    global ruta

    mensaje.set('Abrir fichero')

    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(
            ("Ficheros de texto", "*.txt"),
        ),
        title="Abrir un fichero."
    )


    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        ventana.title(ruta + " - Mi editor")

def guardar():
    mensaje.set('Guardar fichero')

    global ruta
    if ruta != "":
        contenido = texto.get(1.0, 'end')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Fichero guardado correctamente')

def guardar_como():
    print("Guardar fichero como")

    global ruta
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode='w',
                                       defaultextension=".txt")
    ruta = fichero.name
    if fichero is not None:
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Fichero guardado correctamente')
    else:
        mensaje.set('Guardado cancelado')


Archivo = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Archivo", menu = Archivo)
Archivo.add_command(label = "Nuevo", command = nuevo)
Archivo.add_command(label = "Abrir", command = abrir)
Archivo.add_command(label = "Guardar", command = guardar)
Archivo.add_command(label = "Guardar Como", command = guardar_como)

Archivo.add_separator()
Archivo.add_command(label="Salir", command=ventana.quit)


texto = Text(ventana)
texto.pack(fill='both', expand=1)
texto.config(padx=6, pady=4, bd=0, font=("Consolas", 12))

mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(ventana, textvar=mensaje, justify='right')
monitor.pack(side='left')


Editar = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Editar", menu = Editar)
Editar.add_command(label="Cut", \
                   accelerator="Ctrl+X", \
                   command=lambda: \
                            menubar.focus_get().event_generate('<<Cut>>'))
Editar.add_command(label="Copy", \
                   accelerator="Ctrl+C", \
                   command=lambda: \
                             menubar.focus_get().event_generate('<<Copy>>'))
Editar.add_command(label="Pegar", \
                            accelerator="Ctrl+V", \
                            command=lambda: \
                                    menubar.focus_get().event_generate('<<Paste>>'))
Editar.add_command(label = "Buscar")


Editar.add_command(label = "Reemplazar")
Editar.add_separator()




Ejecutar = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Ejecutar", menu = Ejecutar)
Ejecutar.add_command(label = "Analizador Sintactico Ascendente")
Ejecutar.add_command(label = "Analizador Sintactico Descendente")
Ejecutar.add_command(label = "Reportes")
Ejecutar.add_separator()


Opciones = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Opciones", menu = Opciones)
Opciones.add_command(label = "Cambiar Fondo")
Opciones.add_command(label = "Quitar Numero Lineas")
Opciones.add_separator()

Ayuda = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Ayuda", menu = Ayuda)
Ayuda.add_command(label = "Ayuda")
Ayuda.add_command(label = "Acerca de:")
Ayuda.add_separator()

ventana.config(menu = menubar)
ventana.mainloop()