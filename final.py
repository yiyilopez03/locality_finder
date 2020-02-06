#Importamos las librerias que vamos a usar
import numpy as np
import pandas as pd
import tkinter as tk
from funciones import transporte, precio

#Cargamos los archivos de la base de datos desde la carpeta datasets/housing, header = 0 es para indicar el indice
Xdata_suba = pd.read_excel('datasets/housing/suba.xlsx', header = 0)
Xdata_barrios_unidos = pd.read_excel('datasets/housing/barrios_unidos.xlsx', header = 0)
Xdata_bosa = pd.read_excel('datasets/housing/bosa.xlsx', header = 0)
Xdata_engativa = pd.read_excel('datasets/housing/engativa.xlsx', header = 0)
Xdata_teusaquillo = pd.read_excel('datasets/housing/teusaquillo.xlsx', header = 0)
Xdata_usaquen = pd.read_excel('datasets/housing/usaquen.xlsx', header = 0)
Xdata_fontibon = pd.read_excel('datasets/housing/fontibon.xlsx', header = 0)
Xdata_kennedy = pd.read_excel('datasets/housing/kennedy.xlsx', header = 0)
Xdata_puente_aranda = pd.read_excel('datasets/housing/puente_aranda.xlsx', header = 0)
Xdata_san_cristobal = pd.read_excel('datasets/housing/san_cristobal.xlsx', header = 0)
Xdata_santa_fe = pd.read_excel('datasets/housing/santa_fe.xlsx', header = 0)

#Usando la función "precio" que esta en el archivo funciones.py sacamos la columna "PRECIO" de cada base de datos
precio_suba = precio(Xdata_suba)
precio_barrios_unidos = precio(Xdata_barrios_unidos)
precio_bosa = precio(Xdata_bosa)
precio_engativa = precio(Xdata_engativa)
precio_teusaquillo = precio(Xdata_teusaquillo)
precio_usaquen = precio(Xdata_usaquen)
precio_fontibon = precio(Xdata_fontibon)
precio_kennedy = precio(Xdata_kennedy)
precio_puente_aranda = precio(Xdata_puente_aranda)
precio_san_cristobal = precio(Xdata_san_cristobal)
precio_santa_fe = precio(Xdata_santa_fe)

#Sacamos el promedio de los precios de cada base de datos con .mean()
mean_suba = precio_suba.mean()
mean_barrios_unidos = precio_barrios_unidos.mean()
mean_bosa = precio_bosa.mean()
mean_engativa = precio_bosa.mean()
mean_teusaquillo = precio_teusaquillo.mean()
mean_usaquen = precio_usaquen.mean()
mean_fontibon = precio_fontibon.mean()
mean_kennedy = precio_kennedy.mean()
mean_puente_aranda = precio_puente_aranda.mean()
mean_san_cristobal = precio_san_cristobal.mean()
mean_santa_fe = precio_santa_fe.mean()

#Sacamos el precio minimo de la lista de precios de cada base de datos con .min()
min_suba = precio_suba.min()
min_barrios_unidos = precio_barrios_unidos.min()
min_bosa = precio_bosa.min()
min_engativa = precio_bosa.min()
min_teusaquillo = precio_teusaquillo.min()
min_usaquen = precio_usaquen.min()
min_fontibon = precio_fontibon.min()
min_kennedy = precio_kennedy.min()
min_puente_aranda = precio_puente_aranda.min()
min_san_cristobal = precio_san_cristobal.min()
min_santa_fe = precio_santa_fe.min()

#Sacamos el precio máximo de la lista de precios de cada base de datos con .max()
max_suba = precio_suba.max()
max_barrios_unidos = precio_barrios_unidos.max()
max_bosa = precio_bosa.max()
max_engativa = precio_bosa.max()
max_teusaquillo = precio_teusaquillo.max()
max_usaquen = precio_usaquen.max()
max_fontibon = precio_fontibon.max()
max_kennedy = precio_kennedy.max()
max_puente_aranda = precio_puente_aranda.max()
max_san_cristobal = precio_san_cristobal.max()
max_santa_fe = precio_santa_fe.max()

#Definimos la función operaciones para realizar todas las operaciones implementadas en nuesto código
def operaciones():  #Esta función se activa con el botón que creamos casi al final del código

    #Convertimos los datos ingresados por el usuario en su respectivo tipo de variable
    ingresos_data = int(Ingresos.get()) #Ingresos totales del usuario
    workdays_data = int(workdays.get()) #Días trabajados al mes
    transmilenio_data = int(TM.get())  #Veces que usa TM en el día
    answer_transporte_data = str(answer_transporte.get())  #Usa otro medio de transporte "Si/No"
    precio_transporte_data = int(precio_transporte.get())  #Cuando gasta mensual en transporte diferente a TM
    mercado_data = int(Mercado.get())  #Cuanto gasta en mercado mensualmente
    entretenimiento_data = int(Entretenimiento.get())  #Cuanto gasta en actividades diferentes a ya la mencionada

    #Condicional que usamos dependiendo de la respuesta que nos de el usuario a la pregunta de si usa otro medio de transporte
    precio_transporte_final = 0
    if answer_transporte_data == "Si":
        precio_transporte_final = precio_transporte_data
    elif answer_transporte_data == "No":
        precio_transporte_final = 0

    #Calculamos el total gastado en transporte teniendo en cuenta si usa o no otro medio de transporte
    tm_price = (transmilenio_data * 2200) * (workdays_data) #Precio gastado mensual en TM
    #Condicional Si/No al medio de transporte diferente
    answer = answer_transporte_data
    if answer == "Si":
        transport = tm_price + precio_transporte_final
    elif answer == "No":
        transport = tm_price

    arriendo_data = ingresos_data - (transport + mercado_data + entretenimiento_data)  #Dinero que le sobra para el arriendo
    arriendo_text = str(arriendo_data)  #Se convierte esa constante a tipo texto para emplearla después

    total_arriendo = "Dinero restante para tu arriendo: " + arriendo_text #Frase para mostrar en pantalla

    arriendo_label = tk.Label(text = total_arriendo)  #Creamos el texto en pantalla
    arriendo_label.place(x = 22, y = 560)  #Posicionamos en pantalla el recuadro de texto con coordenadas

    mensaje_label = tk.Label(text = "Según tus ingresos y gastos mensuales, puedes vivir en las siguientes localidades: ")  #Creamos el texto en pantalla
    mensaje_label.place(x = 22, y = 580)  #Posicionamos en pantalla el recuadro de texto con coordenadas

    #Utilizamos variables vacías para luego rellenarlas si se cumplen las condiciones
    #Se utiliza "" por que vamos a usa tipo str
    barrios_unidos = ""
    suba = ""
    bosa = ""
    engativa = ""
    teusaquillo = ""
    usaquen = ""
    fontibon = ""
    kennedy = ""
    puente_aranda = ""
    san_cristobal = ""
    santa_fe = ""

    #Condicionales que determinan en que localidad de la ciudad puede vivir dependiendo de lo que le quede para el arriendo
    if arriendo_data > min_barrios_unidos and arriendo_data < max_barrios_unidos:
        barrios_unidos = "Barrios_Unidos "
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
    if arriendo_data > min_fontibon and arriendo_data < max_fontibon:
        fontibon = "Fontibon "
    if arriendo_data > min_kennedy and arriendo_data < max_kennedy:
        kennedy = "Kennedy "
    if arriendo_data > min_puente_aranda and arriendo_data < max_puente_aranda:
        puente_aranda = "Puente_Aranda "
    if arriendo_data > min_san_cristobal and arriendo_data < max_san_cristobal:
        san_cristobal = "San_Cristobal "
    if arriendo_data > min_santa_fe and arriendo_data < max_santa_fe:
        santa_fe = "Santa_Fe "

    #Creamos una variable que incluya las localidades que cumplan la condición para usarla luego
    localidad_text = barrios_unidos + suba + bosa + engativa + teusaquillo +  usaquen + fontibon + kennedy + puente_aranda + san_cristobal + santa_fe

    localidad_label = tk.Label(text = localidad_text)  #Creamos el texto en pantalla con las localidades que cumplieron la condición
    localidad_label.place(x = 22, y = 600)  #Posicionamos el texto en pantalla mediante coordenadas
   
ventana_principal = tk.Tk() #Creamos la ventana principal
ventana_principal.geometry("500x650") #Le damos las dimenciones a la ventana
ventana_principal.resizable(False, False) #Impedimos que se pueda redimencionar la ventana abierta
ventana_principal.title("Calculadora Arriendo") #Título de la ventana
#Titulo que se muestra dentro del programa
main_title = tk.Label(text = "Locality Finder", font = ("Cambria", 13), bg = "#56CD63", fg = "white", width = "550", height = "2")
main_title.pack() #Mostramos el título en pantalla

#Creamos los textos que va a visualizar el usuario en pantalla
ingresos_label = tk.Label(text = "Ingrese sus ingresos mensuales: ")
workdays_label = tk.Label(text = "Ingrese el número de días que trabaja/estudia al mes: ")
transmilenio_label = tk.Label(text = "Ingrese el número de veces que usa TM en el día: ")
question_label = tk.Label(text = "¿Usa otro medio de transporte diferente a TM? (Si/No): ")
precio_transporte_label = tk.Label(text = "Ingrese el valor promedio mensual del precio de transporte diferente al TM: ")
mercado_label = tk.Label(text = "Ingrese su presupuesto para mercado: ")
entretenimiento_label = tk.Label(text = "Ingrese su presupuesto para entretenimiento (Salidas/Comidas/Cine/Fiestas/etc): ")

#Poscionamos los textos en pantalla a través de coordenadas
ingresos_label.place(x = 22, y = 70)
workdays_label.place(x = 22, y = 130)
transmilenio_label.place(x = 22, y = 190)
question_label.place(x = 22, y = 250)
precio_transporte_label.place(x = 22, y = 310)
mercado_label.place(x = 22, y = 370)
entretenimiento_label.place(x = 22, y = 430)

#Creamos las variables de los datos que el usuario va a digitar
Ingresos = tk.IntVar()
workdays = tk.IntVar()
answer_transporte = tk.StringVar()
precio_transporte = tk.IntVar()
TM = tk.IntVar()
Mercado = tk.IntVar()
Entretenimiento = tk.IntVar()

#Creamos los cajones donde el usuario va a ingresar los datos dentro del programa
ingresos_entry = tk.Entry(textvariable = Ingresos, width = "40")
workdays_entry = tk.Entry(textvariable = workdays, width = "40")
transmilenio_entry = tk.Entry(textvariable = TM, width = "40")
answer_entry = tk.Entry(textvariable = answer_transporte, width = "40")
precio_transporte_entry = tk.Entry(textvariable = precio_transporte, width = "40")
mercado_entry = tk.Entry(textvariable = Mercado, width = "40")
entretenimiento_entry = tk.Entry(textvariable = Entretenimiento, width = "40")

#Posicionamos los cajones de entrada en la pantalla utilizando coordenadas
ingresos_entry.place(x = 22, y = 100)
workdays_entry.place(x = 22, y = 160)
transmilenio_entry.place(x = 22, y = 220)
answer_entry.place(x = 22, y = 280)
precio_transporte_entry.place(x = 22, y = 340)
mercado_entry.place(x = 22, y = 400)
entretenimiento_entry.place(x = 22, y = 460)

#Creamos el botón de confirmación que activa la función "operaciones" para arrojar los resultados en pantalla
confirmar_btn = tk.Button(ventana_principal, text = "Confirmar", command = operaciones, width = "30", height = "1")
confirmar_btn.place(x = 22, y = 510) #Posicionamos el botón en pantalla

ventana_principal.mainloop() #Hace que el programa no se cierre solo después de ejecutarlo