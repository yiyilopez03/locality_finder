import numpy as np
import pandas as pd
import tkinter as tk
from funciones import transporte, completar

csv_path = 'datasets/housing/housing.csv'
csv_suba = 'datasets/housing/suba.csv'
csv_barrios_unidos = 'datasets/housing/barrios_unidos.csv'
csv_bosa = 'datasets/housing/bosa.csv' 
csv_engativa = 'datasets/housing/engativa.csv'
csv_teusaquillo = 'datasets/housing/teusaquillo.csv'
csv_usaquen = 'datasets/housing/usaquen.csv'

Xdata = pd.read_csv(csv_path)
Xdata_suba = pd.read_csv(csv_suba)
Xdata_barrios_unidos = pd.read_csv(csv_barrios_unidos)
Xdata_bosa = pd.read_csv(csv_bosa)
Xdata_engativa = pd.read_csv(csv_engativa)
Xdata_teusaquillo = pd.read_csv(csv_teusaquillo)
Xdata_usaquen = pd.read_csv(csv_usaquen)

#Completar faltantes
Xdata_suba = completar(Xdata_suba)
Xdata_barrios_unidos = completar(Xdata_barrios_unidos)
Xdata_bosa = completar(Xdata_bosa)
Xdata_engativa = completar(Xdata_engativa)
Xdata_teusaquillo = completar(Xdata_teusaquillo)
Xdata_usaquen = completar(Xdata_usaquen)

median_suba = Xdata_suba["precio"].median()
median_barrios_unidos = Xdata_barrios_unidos["precio"].median()
median_bosa = Xdata_bosa["precio"].median()
median_engativa = Xdata_engativa["precio"].median()
median_teusaquillo = Xdata_teusaquillo["precio"].median()
median_usaquen = Xdata_usaquen["precio"].median()

min_suba = Xdata_suba["precio"].min()
min_barrios_unidos = Xdata_barrios_unidos["precio"].median()
min_bosa = Xdata_bosa["precio"].min()
min_engativa = Xdata_engativa["precio"].min()
min_teusaquillo = Xdata_teusaquillo["precio"].min()
min_usaquen = Xdata_usaquen["precio"].min()

max_suba = Xdata_suba["precio"].max()
max_barrios_unidos = Xdata_barrios_unidos["precio"].max()
max_bosa = Xdata_bosa["precio"].max()
max_engativa = Xdata_engativa["precio"].max()
max_teusaquillo = Xdata_teusaquillo["precio"].max()
max_usaquen = Xdata_usaquen["precio"].max()

def operaciones():
    ingresos_data = int(Ingresos.get())
    workdays_data = int(workdays.get())
    transmilenio_data = int(TM.get())
    answer_transporte_data = str(answer_transporte.get())
    precio_transporte_data = int(precio_transporte.get())
    mercado_data = int(Mercado.get())
    entretenimiento_data = int(Entretenimiento.get())

    precio_transporte_final = 0
    if answer_transporte_data == "Si":
        precio_transporte_final = precio_transporte_data
    elif answer_transporte_data == "No":
        precio_transporte_final = 0

    tm_price = (transmilenio_data * 2200) * (workdays_data)
    answer = answer_transporte_data
    if answer == "Si":
        transport = tm_price + precio_transporte_final
    elif answer == "No":
        transport = tm_price

    arriendo_data = ingresos_data - (transport + mercado_data + entretenimiento_data)
    arriendo_text = str(arriendo_data)

    total_arriendo = "Dinero restante para tu arriendo: " + arriendo_text

    arriendo_label = tk.Label(text = total_arriendo)
    arriendo_label.place(x = 22, y = 560)

    mensaje_label = tk.Label(Text = "Según tus ingresos y gastos mensuales, puedes vivir en las siguientes localidades: ")
    mensaje_label.place(x = 22, y = 580)

    barrios_unidos = ""
    suba = ""
    bosa = ""
    engativa = ""
    teusaquillo = ""
    usaquen = ""

    if arriendo_data > min_barrios_unidos and arriendo_data < max_barrios_unidos:
        barrios_unidos = "Barrios unidos "
    if arriendo_data > min_suba and arriendo_data < max_suba:
        suba = "Suba "
    if arriendo_data > min_bosa and arriendo_data < max_bosa:
        bosa = "Bosa "
    if arriendo_data > min_engativa and arriendo_data < max_engativa:
        engativa = "Engativa "
    if arriendo_data > min_teusaquillo and arriendo_data < max_teusaquillo:
        teusaquillo = "Teusaquillo "
    if arriendo_data > min_usaquen and arriendo_data < max_usaquen:
        usaquen = "Usaquen "

    localidad_text = barrios_unidos + suba + bosa + engativa + teusaquillo +  usaquen

    localidad_label = tk.Label(text = localidad_text)
    localidad_label.place(x = 22, y = 600)
   
    print(ingresos_data, "\t", workdays_data, "\t", transmilenio_data, "\t", answer_transporte_data, "\t", precio_transporte_data, "\t",  mercado_data, "\t", entretenimiento_data)
    print("Precio total transporte: ", transport, "\t", "Dinero restantes para el arriendo: ", total_arriendo)


ventana_principal = tk.Tk()
ventana_principal.geometry("500x650")
ventana_principal.resizable(False, False)
ventana_principal.title("Calculadora Arriendo")
main_title = tk.Label(text = "Calculadora Arriendo | Project A", font = ("Cambria", 13), bg = "#56CD63", fg = "white", width = "550", height = "2")
main_title.pack()

ingresos_label = tk.Label(text = "Ingrese sus ingresos mensuales: ")
workdays_label = tk.Label(text = "Ingrese el número de días que trabaja/estudia a la semana: ")
transmilenio_label = tk.Label(text = "Ingrese el número de veces que usa TM en el día: ")
question_label = tk.Label(text = "¿Usa otro medio de transporte diferente a TM? (Si/No): ")
precio_transporte_label = tk.Label(text = "Ingrese el valor promedio mensual del precio de transporte diferente al TM: ")
mercado_label = tk.Label(text = "Ingrese su presupuesto para mercado: ")
entretenimiento_label = tk.Label(text = "Ingrese su presupuesto para entretenimiento (Salidas/Comidas/Cine/Fiestas/etc): ")

ingresos_label.place(x = 22, y = 70)
workdays_label.place(x = 22, y = 130)
transmilenio_label.place(x = 22, y = 190)
question_label.place(x = 22, y = 250)
precio_transporte_label.place(x = 22, y = 310)
mercado_label.place(x = 22, y = 370)
entretenimiento_label.place(x = 22, y = 430)

Ingresos = tk.IntVar()
workdays = tk.IntVar()
answer_transporte = tk.StringVar()
precio_transporte = tk.IntVar()
TM = tk.IntVar()
Mercado = tk.IntVar()
Entretenimiento = tk.IntVar()

ingresos_entry = tk.Entry(textvariable = Ingresos, width = "40")
workdays_entry = tk.Entry(textvariable = workdays, width = "40")
transmilenio_entry = tk.Entry(textvariable = TM, width = "40")
answer_entry = tk.Entry(textvariable = answer_transporte, width = "40")
precio_transporte_entry = tk.Entry(textvariable = precio_transporte, width = "40")
mercado_entry = tk.Entry(textvariable = Mercado, width = "40")
entretenimiento_entry = tk.Entry(textvariable = Entretenimiento, width = "40")

ingresos_entry.place(x = 22, y = 100)
workdays_entry.place(x = 22, y = 160)
transmilenio_entry.place(x = 22, y = 220)
answer_entry.place(x = 22, y = 280)
precio_transporte_entry.place(x = 22, y = 340)
mercado_entry.place(x = 22, y = 400)
entretenimiento_entry.place(x = 22, y = 460)

confirmar_btn = tk.Button(ventana_principal, text = "Confirmar", command = operaciones, width = "30", height = "1")
confirmar_btn.place(x = 22, y = 510)

ventana_principal.mainloop()