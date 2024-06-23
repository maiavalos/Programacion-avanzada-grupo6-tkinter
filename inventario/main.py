import tkinter as tk
from gui import InventoryApp

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    app.pack()
    root.mainloop()
