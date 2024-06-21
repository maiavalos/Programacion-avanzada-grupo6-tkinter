from tkinter import *

raiz = Tk()
raiz.title('UNaB - Universidad Nacional Guillermo Brown')

# BARRA DE MENÚ
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label='Conectar')
bbddmenu.add_command(label='Salir')

borrarmenu = Menu(barramenu, tearoff=0)
borrarmenu.add_command(label="Limpiar")

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="Acerca de...")

barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Limpiar", menu=borrarmenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

# FRAME CAMPOS
framecampos = Frame(raiz)
framecampos.pack()

legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

legajo_input = Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=1, padx=10, pady=10)

alumno_input = Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=1, column=1, padx=10, pady=10)

email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=1, padx=10, pady=10)

calificacion_input = Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=3, column=1, padx=10, pady=10)

escuela_input = Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=4, column=1, padx=10, pady=10)

localidad_input = Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=5, column=1, padx=10, pady=10)

provincia_input = Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=6, column=1, padx=10, pady=10)

# LABELS
legajolabel = Label(framecampos, text="Legajo:")
legajolabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

alumnolabel = Label(framecampos, text="Alumno:")
alumnolabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

emaillabel = Label(framecampos, text="Email:")
emaillabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

calificacionlabel = Label(framecampos, text="Calificación:")
calificacionlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

carreralabel = Label(framecampos, text="Carrera:")
carreralabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

localidadlabel = Label(framecampos, text="Localidad:")
localidadlabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

provincialabel = Label(framecampos, text="Provincia:")
provincialabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

# FRAME BOTONERA
framebotones = Frame(raiz)
framebotones.pack()

boton_crear = Button(framebotones, text="Crear")
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer = Button(framebotones, text="Leer")
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar = Button(framebotones, text="Actualizar")
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar = Button(framebotones, text="Borrar")
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

# FRAME PIE
framecopy = Frame(raiz)
framecopy.pack()
copylabel = Label(framecopy, text=" Prog. Avanzada / Prof. Felipe Morales /Alumnos: Avalos - Pérez Veltri - Euler ")
copylabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)


raiz.mainloop()