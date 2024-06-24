import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")

        self.contador = 0

        
        self.marco_principal = tk.Frame(root)
        self.marco_principal.pack(pady=20)

        
        self.label = tk.Label(self.marco_principal, text=self.contador, font=("Helvetica", 24))
        self.label.pack()

       
        self.btn_sumar = tk.Button(self.marco_principal, text="+", font=("Helvetica", 18), command=self.sumar, padx=20, pady=10)
        self.btn_sumar.pack(side=tk.LEFT, padx=10)

        self.btn_restar = tk.Button(self.marco_principal, text="-", font=("Helvetica", 18), command=self.restar, padx=20, pady=10)
        self.btn_restar.pack(side=tk.LEFT, padx=10)

        self.btn_reiniciar = tk.Button(self.marco_principal, text="Reiniciar", font=("Helvetica", 18), command=self.reiniciar, padx=20, pady=10)
        self.btn_reiniciar.pack(side=tk.LEFT, padx=10)

        self.label_info = tk.Label(root, text="Prog. Avanzada / Prof. Felipe Morales / Alumnos: Avalos - Pérez Veltri - Euler", font=("Helvetica", 10), fg="gray")
        self.label_info.pack(pady=(0, 20))  

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
