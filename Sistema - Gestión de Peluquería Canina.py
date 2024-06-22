import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Datos de ejemplo
citas = []
clientes = {}
servicios = {"Corte de Pelo": 7500.0, "Baño": 2000.0, "Corte de Uñas": 1500.0}

# Funciones
def programar_cita():
    # Obtener los valores ingresados por el usuario en los campos de entrada
    nombre_cliente = entrada_nombre_cliente.get()
    tipo_servicio = entrada_tipo_servicio.get()
    fecha_cita = entrada_fecha_cita.get()

    # Verificar que todos los campos estén llenos
    if nombre_cliente and tipo_servicio and fecha_cita:
        # Agregar la cita a la lista de citas
        citas.append({"nombre_cliente": nombre_cliente, "tipo_servicio": tipo_servicio, "fecha_cita": fecha_cita})
        # Mostrar mensaje de confirmación
        messagebox.showinfo("Cita Programada", f"Cita programada para {nombre_cliente}")
    else:
        # Mostrar mensaje de error si algún campo está vacío
        messagebox.showerror("Error", "Todos los campos son obligatorios")

def ver_citas():
    # Crear una nueva ventana para mostrar las citas programadas
    ventana_citas = tk.Toplevel(root)
    ventana_citas.title("Citas Programadas")

    # Crear una lista para mostrar las citas
    lista_citas = tk.Listbox(ventana_citas)
    lista_citas.pack(fill=tk.BOTH, expand=True)
    
    # Recorrer la lista de citas y agregarlas a la lista visual
    for cita in citas:
        lista_citas.insert(tk.END, f"Cliente: {cita['nombre_cliente']}, Servicio: {cita['tipo_servicio']}, Fecha: {cita['fecha_cita']}")

def gestionar_clientes():
    # Crear una nueva ventana para la gestión de clientes
    ventana_clientes = tk.Toplevel(root)
    ventana_clientes.title("Gestión de Clientes")

    # Crear una lista para mostrar los clientes
    lista_clientes = tk.Listbox(ventana_clientes)
    lista_clientes.pack(fill=tk.BOTH, expand=True)
    
    # Recorrer el diccionario de clientes y agregarlos a la lista visual
    for cliente, detalles in clientes.items():
        lista_clientes.insert(tk.END, f"Nombre: {cliente}, Detalles: {detalles}")

def gestionar_servicios():
    # Crear una nueva ventana para la gestión de servicios
    ventana_servicios = tk.Toplevel(root)
    ventana_servicios.title("Gestión de Servicios")

    # Crear una lista para mostrar los servicios
    lista_servicios = tk.Listbox(ventana_servicios)
    lista_servicios.pack(fill=tk.BOTH, expand=True)
    
    # Recorrer el diccionario de servicios y agregarlos a la lista visual
    for servicio, precio in servicios.items():
        lista_servicios.insert(tk.END, f"Servicio: {servicio}, Precio: ${precio}")

# Interfaz de Usuario
root = tk.Tk()
root.title("Pulgas Glam - Sistema de Gestión de Peluquería Canina")

# Crear la barra de menú
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Submenú de base de datos
menu_bbdd = tk.Menu(barra_menu, tearoff=0)
menu_bbdd.add_command(label='Conectar')
menu_bbdd.add_command(label='Salir')

# Submenú de limpieza
menu_limpiar = tk.Menu(barra_menu, tearoff=0)
menu_limpiar.add_command(label="Limpiar")

# Submenú de ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Licencia")
menu_ayuda.add_command(label="Acerca de...")

# Agregar los submenús a la barra de menú
barra_menu.add_cascade(label="BBDD", menu=menu_bbdd)
barra_menu.add_cascade(label="Limpiar", menu=menu_limpiar)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Título del negocio
etiqueta_nombre_negocio = tk.Label(root, text="Pulgas Glam", font=("Helvetica", 16, "bold"))
etiqueta_nombre_negocio.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Marco para programar citas
marco_cita = ttk.LabelFrame(root, text="Programar Cita")
marco_cita.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Etiqueta y campo de entrada para el nombre del cliente
tk.Label(marco_cita, text="Nombre del Cliente:").grid(row=0, column=0, padx=5, pady=5)
entrada_nombre_cliente = tk.Entry(marco_cita)
entrada_nombre_cliente.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de entrada para el tipo de servicio
tk.Label(marco_cita, text="Tipo de Servicio:").grid(row=1, column=0, padx=5, pady=5)
entrada_tipo_servicio = tk.Entry(marco_cita)
entrada_tipo_servicio.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta y campo de entrada para la fecha de la cita
tk.Label(marco_cita, text="Fecha de la Cita (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
entrada_fecha_cita = tk.Entry(marco_cita)
entrada_fecha_cita.grid(row=2, column=1, padx=5, pady=5)

# Botón para programar la cita
tk.Button(marco_cita, text="Programar Cita", command=programar_cita).grid(row=3, column=0, columnspan=2, pady=10)

# Botón para ver citas programadas
tk.Button(root, text="Ver Citas Programadas", command=ver_citas).grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# Botón para gestionar clientes
tk.Button(root, text="Gestión de Clientes", command=gestionar_clientes).grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# Botón para gestionar servicios
tk.Button(root, text="Gestión de Servicios", command=gestionar_servicios).grid(row=4, column=0, padx=10, pady=5, sticky="ew")

# Pie de página con información del curso y los alumnos
frame_copy = tk.Frame(root)
frame_copy.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
etiqueta_copy = tk.Label(frame_copy, text=" Prog. Avanzada / Prof. Felipe Morales / Alumnos: Avalos - Pérez Veltri - Euler ")
etiqueta_copy.grid(row=0, column=0, sticky="e")

# Iniciar el bucle principal de la aplicación
root.mainloop()
