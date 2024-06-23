Sistema de Inventario con Tkinter

Este proyecto implementa un sistema de gestión de inventario simple utilizando Python y Tkinter para la interfaz gráfica de usuario (GUI).
Perfecto para comercios chiquitos, o para situaciones donde se requiera un inventario simple.

Requisitos
Python 3.x instalado.
Biblioteca Tkinter incluida en la instalación estándar de Python.

Instalación y Ejecución
1-descargar la carpeta inventario
2-Ejecutar la aplicación .exe

Funcionalidades
La aplicación permite realizar las siguientes operaciones:

Agregar Producto: Permite añadir un nuevo producto al inventario especificando nombre y cantidad.
Modificar Producto: Permite modificar la cantidad de un producto existente en el inventario.
Eliminar Producto: Permite eliminar un producto del inventario.
Buscar Producto: Permite buscar un producto en el inventario por su nombre.
Mostrar Inventario: Muestra todos los productos actuales en el inventario y además, los separa en los productos con menos de 5 y con mas de 5 unidades.
Cada funcionalidad está implementada en pestañas separadas dentro de la interfaz de usuario para una mejor organización y navegación.

Estructura del Proyecto
El proyecto está organizado en los siguientes archivos principales:
main.py: Punto de entrada del programa. Inicializa la aplicación Tkinter y la instancia de InventoryApp.
gui.py: Define la clase InventoryApp que construye la interfaz gráfica utilizando Tkinter y maneja los eventos de los botones y entradas.
inventory.py: Contiene la clase Inventory que gestiona los datos del inventario, incluyendo métodos para añadir, modificar, eliminar productos y obtener el inventario actual.