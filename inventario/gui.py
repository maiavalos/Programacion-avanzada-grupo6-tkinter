
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from inventory import Inventory

class InventoryApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Sistema de Inventario")
        self.inventory = Inventory()
        self.create_widgets()
    def add_product(self):
        name = self.entry_name_add.get()
        quantity = self.entry_quantity_add.get()
        if name and quantity:
            try:
                quantity = int(quantity)
                self.inventory.add_product(name, quantity)
                self.check_inventory_alert(name, quantity)
                messagebox.showinfo("Éxito", f"Producto '{name}' agregado al inventario.")
                self.entry_name_add.delete(0, tk.END)
                self.entry_quantity_add.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        else:
            messagebox.showerror("Error", "Por favor ingrese el nombre y la cantidad del producto.")

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tab_add = tk.Frame(self.notebook)
        self.notebook.add(self.tab_add, text="Agregar Producto")
        self.create_add_widgets()

        self.tab_modify = tk.Frame(self.notebook)
        self.notebook.add(self.tab_modify, text="Modificar Producto")
        self.create_modify_widgets()

        self.tab_remove = tk.Frame(self.notebook)
        self.notebook.add(self.tab_remove, text="Eliminar Producto")
        self.create_remove_widgets()

        self.tab_search = tk.Frame(self.notebook)
        self.notebook.add(self.tab_search, text="Buscar Producto")
        self.create_search_widgets()

        self.tab_show = tk.Frame(self.notebook)
        self.notebook.add(self.tab_show, text="Mostrar Inventario")
        self.create_show_widgets()

    def create_add_widgets(self):

        self.label_name_add = tk.Label(self.tab_add, text="Nombre del Producto:")
        self.label_name_add.pack(pady=5)
        self.entry_name_add = tk.Entry(self.tab_add)
        self.entry_name_add.pack(pady=5)

    
        self.label_quantity_add = tk.Label(self.tab_add, text="Cantidad:")
        self.label_quantity_add.pack(pady=5)
        self.entry_quantity_add = tk.Entry(self.tab_add)
        self.entry_quantity_add.pack(pady=5)

        
        self.button_add = tk.Button(self.tab_add, text="Agregar Producto", command=self.add_product)
        self.button_add.pack(pady=10)

    def create_modify_widgets(self):
        self.label_name_modify = tk.Label(self.tab_modify, text="Nombre del Producto:")
        self.label_name_modify.pack(pady=5)
        self.entry_name_modify = tk.Entry(self.tab_modify)
        self.entry_name_modify.pack(pady=5)

        self.label_quantity_modify = tk.Label(self.tab_modify, text="Nueva Cantidad:")
        self.label_quantity_modify.pack(pady=5)
        self.entry_quantity_modify = tk.Entry(self.tab_modify)
        self.entry_quantity_modify.pack(pady=5)

        self.button_modify = tk.Button(self.tab_modify, text="Modificar Cantidad", command=self.modify_quantity)
        self.button_modify.pack(pady=10)

    def create_remove_widgets(self):
        self.label_name_remove = tk.Label(self.tab_remove, text="Nombre del Producto:")
        self.label_name_remove.pack(pady=5)
        self.entry_name_remove = tk.Entry(self.tab_remove)
        self.entry_name_remove.pack(pady=5)

        self.button_remove = tk.Button(self.tab_remove, text="Eliminar Producto", command=self.remove_product)
        self.button_remove.pack(pady=10)

    def create_search_widgets(self):
        self.label_search = tk.Label(self.tab_search, text="Buscar Producto:")
        self.label_search.pack(pady=5)
        self.entry_search = tk.Entry(self.tab_search)
        self.entry_search.pack(pady=5)

   
        self.button_search = tk.Button(self.tab_search, text="Buscar", command=self.search_product)
        self.button_search.pack(pady=10)

    def create_show_widgets(self):
        self.button_show = tk.Button(self.tab_show, text="Mostrar Inventario", command=self.show_inventory)
        self.button_show.pack(pady=10)

    def add_product(self):
        name = self.entry_name_add.get()
        quantity = self.entry_quantity_add.get()
        if name and quantity:
            try:
                quantity = int(quantity)
                self.inventory.add_product(name, quantity)
                self.check_inventory_alert(name, quantity)
                messagebox.showinfo("Éxito", f"Producto '{name}' agregado al inventario.")
                self.entry_name_add.delete(0, tk.END)
                self.entry_quantity_add.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        else:
            messagebox.showerror("Error", "Por favor ingrese el nombre y la cantidad del producto.")

    def modify_quantity(self):
        name = self.entry_name_modify.get()
        quantity = self.entry_quantity_modify.get()
        if name and quantity:
            try:
                quantity = int(quantity)
                self.inventory.modify_quantity(name, quantity)
                self.check_inventory_alert(name, quantity)
                messagebox.showinfo("Éxito", f"Cantidad de '{name}' modificada correctamente.")
                self.entry_name_modify.delete(0, tk.END)
                self.entry_quantity_modify.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        else:
            messagebox.showerror("Error", "Por favor ingrese el nombre y la nueva cantidad del producto.")

    def remove_product(self):
        name = self.entry_name_remove.get()
        if name:
            if name in self.inventory.get_inventory():
                self.inventory.remove_product(name)
                messagebox.showinfo("Éxito", f"Producto '{name}' eliminado del inventario.")
            else:
                messagebox.showerror("Error", f"No se encontró el producto '{name}' en el inventario.")
        else:
            messagebox.showerror("Error", "Por favor ingrese el nombre del producto a eliminar.")

    def search_product(self):
        search_term = self.entry_search.get()
        if search_term:
            if search_term in self.inventory.get_inventory():
                quantity = self.inventory.get_inventory()[search_term]
                messagebox.showinfo("Producto Encontrado", f"{search_term}: {quantity}")
            else:
                messagebox.showinfo("Producto no encontrado", f"No se encontró el producto '{search_term}' en el inventario.")
        else:
            messagebox.showerror("Error", "Por favor ingrese un término de búsqueda.")

    def show_inventory(self):
        above_five, below_five = self.inventory.split_inventory()

        if above_five or below_five:
            message = ""

            if above_five:
                message += "Productos con 5 o más unidades:\n"
                message += "\n".join(f"{name}: {quantity}" for name, quantity in above_five)
                message += "\n\n"

            if below_five:
                message += "Productos con menos de 5 unidades:\n"
                message += "\n".join(f"{name}: {quantity}" for name, quantity in below_five)

            messagebox.showinfo("Inventario", message)
        else:
            messagebox.showinfo("Inventario", "El inventario está vacío.")

    

    def check_inventory_alert(self, name, quantity):
        if quantity < 5:
            messagebox.showwarning("Alerta de Inventario", f"¡Alerta! Quedan menos de 5 unidades de '{name}'.")

