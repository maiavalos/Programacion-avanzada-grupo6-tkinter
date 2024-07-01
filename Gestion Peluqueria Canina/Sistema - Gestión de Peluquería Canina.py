import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Servicio:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Cita:
    def __init__(self, cliente, servicio, fecha):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha

class SistemaGestion:
    def __init__(self):
        self.citas = []
        self.clientes = {}
        self.servicios = {"Corte de Pelo": Servicio("Corte de Pelo", 7500.0), 
                          "Baño": Servicio("Baño", 2000.0), 
                          "Corte de Uñas": Servicio("Corte de Uñas", 1500.0)}
    
    def programar_cita(self, nombre_cliente, tipo_servicio, fecha_cita):
        if nombre_cliente and tipo_servicio and fecha_cita:
            cliente = self.clientes.get(nombre_cliente, Cliente(nombre_cliente))
            servicio = self.servicios.get(tipo_servicio, None)
            if servicio:
                cita = Cita(cliente, servicio, fecha_cita)
                self.citas.append(cita)
                messagebox.showinfo("Cita Programada", f"Cita programada para {cliente.nombre}")
            else:
                messagebox.showerror("Error", "Servicio no encontrado")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
    
    def ver_citas(self):
        ventana_citas = tk.Toplevel(root)
        ventana_citas.title("Citas Programadas")
        lista_citas = tk.Listbox(ventana_citas)
        lista_citas.pack(fill=tk.BOTH, expand=True)
        
        for cita in self.citas:
            lista_citas.insert(tk.END, f"Cliente: {cita.cliente.nombre}, Servicio: {cita.servicio.nombre}, Fecha: {cita.fecha}")
    
    def gestionar_clientes(self):
        ventana_clientes = tk.Toplevel(root)
        ventana_clientes.title("Gestión de Clientes")
        lista_clientes = tk.Listbox(ventana_clientes)
        lista_clientes.pack(fill=tk.BOTH, expand=True)
        
        for cliente in self.clientes.values():
            lista_clientes.insert(tk.END, f"Nombre: {cliente.nombre}")

    def gestionar_servicios(self):
        ventana_servicios = tk.Toplevel(root)
        ventana_servicios.title("Gestión de Servicios")
        lista_servicios = tk.Listbox(ventana_servicios)
        lista_servicios.pack(fill=tk.BOTH, expand=True)
        
        for servicio in self.servicios.values():
            lista_servicios.insert(tk.END, f"Servicio: {servicio.nombre}, Precio: ${servicio.precio}")

# Crear una instancia del sistema de gestión
sistema_gestion = SistemaGestion()

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
tk.Button(marco_cita, text="Programar Cita", command=lambda: sistema_gestion.programar_cita(entrada_nombre_cliente.get(), entrada_tipo_servicio.get(), entrada_fecha_cita.get())).grid(row=3, column=0, columnspan=2, pady=10)

# Botón para ver citas programadas
tk.Button(root, text="Ver Citas Programadas", command=sistema_gestion.ver_citas).grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# Botón para gestionar clientes
tk.Button(root, text="Gestión de Clientes", command=sistema_gestion.gestionar_clientes).grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# Botón para gestionar servicios
tk.Button(root, text="Gestión de Servicios", command=sistema_gestion.gestionar_servicios).grid(row=4, column=0, padx=10, pady=5, sticky="ew")

# Pie de página con información del curso y los alumnos
frame_copy = tk.Frame(root)
frame_copy.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
etiqueta_copy = tk.Label(frame_copy, text="Prog. Avanzada / Prof. Felipe Morales / Alumnos: Avalos - Pérez Veltri - Euler")
etiqueta_copy.grid(row=0, column=0, sticky="e")

# Iniciar el bucle principal de la aplicación
root.mainloop()
