from tkinter import messagebox, Label, Button, Entry, Tk
import requests
import tkinter as tk
from datetime import datetime, timedelta

# 153c99cee77762eb132a11d5891e8479
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# VENTANA PRINCIPAL
ventana = Tk()
ventana.configure(bg= "deepskyblue")
ventana.geometry("1000x500")
ventana.title("APLICACION DEL CLIMA CON ZONA HORARIA")
ventana.resizable(False, False)


# FUNCION PARA LLAMAR A LA API
def clima_App(ciudad):
    try:
        API_key = "153c99cee77762eb132a11d5891e8479"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPid" : API_key, "q" : ciudad, "units" : "metric", "lang" : "es"}
        respuesta = requests.get(URL, params=parametros)
        fondo_labels.place(x=0, y=125, width=1000, height=400)
        fondo_ciudad.place(x=0, y=125, width=1000, height=50)
        copylabel.place(relx=0.5, rely=0.98, anchor="center")
        mostrar_labels()
        clima = respuesta.json()
        
    except:
        print("ERROR")

    mostar_clima(clima)
    mostar_hora_zona(clima)


# FUNCION PARA MOSTRAR EL CLIMA
def mostrar_labels():
    ciudad.place(relx=0.5, rely=0.3, anchor='center')

    temp_clima.place(x=55, y=200)
    temp_clima_text.place(x=20, y=180)

    descrip_clima.place(x=55, y=330)
    descrip_clima_text.place(x=20, y=305)


    zona_horaria.place(x=753, y=220)
    zona_horaria_text.place(x=790, y=180)


def mostar_clima(clima):
    try:
        ciudad_nom = clima["name"]
        temperatura = clima["main"]["temp"]
        desc = clima["weather"][0]["description"]


        ciudad["text"] = ciudad_nom 
        temp_clima["text"] = str(int(temperatura)) + "°C"
        descrip_clima["text"] = desc

    except:

        ciudad.place_forget()

        descrip_clima.place_forget()
        descrip_clima_text.place_forget()

        temp_clima.place_forget()
        temp_clima_text.place_forget()

        zona_horaria.place_forget()
        zona_horaria_text.place_forget()

        fondo_labels.place_forget()
        fondo_ciudad.place_forget()

        copylabel.place_forget()

        messagebox.showerror("CIUDAD INCORRECTA", "ERROR: Ese Lugar No Existe!\n      Intentalo De Nuevo!")


# FUNCION PARA MOSTRAR LA HORA          
def mostar_hora_zona(clima):
    try:
        ciudad_hora = clima["timezone"]
        hora_utc = datetime.utcnow()
        desplazamiento_segundos = ciudad_hora

        hora_local = hora_utc + timedelta(seconds=desplazamiento_segundos)
        hora_formateada_local = hora_local.strftime("%I:%M %p")
        zona_horaria["text"] = hora_formateada_local


    except:
        zona_horaria["text"] = " "




#INTERFAZ

# """ Barra de Busqueda """
text1 = Label(ventana, text="Bucar Continente/País/Ciudad/Localidad:", font=("univers LT Std 47 Cn Lt", 10, "bold"), bg="deepskyblue", fg="black")
text1.place(relx=0.5, rely=0.06, anchor="center")

buscar_ciudad = Entry(ventana, font = ("Courier New", 20, "bold"), relief="flat", highlightbackground="black", highlightthickness=3, justify= "center", bg="white", fg="black")
buscar_ciudad.place(relx=0.5, rely=0.11, width=300, height=30, anchor="center")
buscar_ciudad.focus()


# """ Botón Buscar """
obtener_clima = Button(ventana, text="Buscar", bg="pink", cursor="hand2", command=lambda:clima_App(buscar_ciudad.get()))
obtener_clima.place(relx=0.68, rely=0.11, width=50, height=30, anchor="center")


# """ PONER OTRO FONDO """
fondo_labels = tk.Frame(ventana, bg="deepskyblue3", borderwidth=0, relief="solid")
fondo_ciudad = tk.Frame(ventana, bg="deepskyblue4", borderwidth=1, relief="solid")


# """ Clima/Temperatura/ETC """
ciudad = tk.Label(font=("aquire", 20, "bold"), bg="deepskyblue4", fg="white")


temp_clima = tk.Label(font=("aquire", 50, "bold"), bg="deepskyblue3", fg="white")
temp_clima_text = tk.Label(text="Temperatura Actual", font=("univers LT Std 47 Cn Lt", 15, "bold"), bg="deepskyblue3", fg="white")

descrip_clima = tk.Label(font=("aquire", 20, "bold"), bg="deepskyblue3", fg="white")
descrip_clima_text = tk.Label(text="Detalles:", font=("univers LT Std 47 Cn Lt", 10, "bold"), bg="deepskyblue3", fg="white")


# """ ZONA HORARIA """
zona_horaria = tk.Label(font=("aquire", 40, "bold"), bg="deepskyblue3", fg="white")
zona_horaria_text = tk.Label(text="Hora Actual", font=("univers LT Std 47 Cn Lt", 20, "bold"), bg="deepskyblue3", fg="white")

# """ INTEGRANTES """
copylabel = Label(text="Prog. Avanzada / Prof. Felipe Morales / Alumnos: Avalos - Pérez Veltri - Euler", bg="deepskyblue3")

ventana.mainloop()
