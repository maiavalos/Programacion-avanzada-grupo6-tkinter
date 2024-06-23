import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")

        self.contador = 0

        self.label = tk.Label(root, text=self.contador, font=("Helvetica", 24))
        self.label.pack(pady=20)

        # Botones para sumar, restar y reiniciar con tamaño más grande
        self.btn_sumar = tk.Button(root, text="+", font=("Helvetica", 18), command=self.sumar, padx=20, pady=10)
        self.btn_sumar.pack(side=tk.LEFT, padx=10)

        self.btn_restar = tk.Button(root, text="-", font=("Helvetica", 18), command=self.restar, padx=20, pady=10)
        self.btn_restar.pack(side=tk.LEFT, padx=10)

        self.btn_reiniciar = tk.Button(root, text="Reiniciar", font=("Helvetica", 18), command=self.reiniciar, padx=20, pady=10)
        self.btn_reiniciar.pack(side=tk.LEFT, padx=10)

    def sumar(self):
        self.contador += 1
        self.actualizar_label()

    def restar(self):
        self.contador -= 1
        self.actualizar_label()

    def reiniciar(self):
        self.contador = 0
        self.actualizar_label()

    def actualizar_label(self):
        self.label.config(text=self.contador)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()
