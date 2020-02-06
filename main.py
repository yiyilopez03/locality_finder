import numpy as np
import pandas as pd
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
precio_suba = (precio(Xdata_suba))
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

#Definimos variables
Ingresos = int(input("Ingrese sus ingresos mensuales: "))
workdays = int(input("Ingrese el número de días que trabaja/estudia al mes: "))
tm = int(input("Ingrese el número de veces que usa TM en el día: "))

#Condicional para la pregunta del transporte
answer_transporte = " "
while answer_transporte != "Si" or "No":
    answer_transporte = str(input("¿Usa otro medio de transporte diferente a TM?: "))
    if answer_transporte == "Si" or "No":
        break
    else:
        print("Digíte una respuesta Si/No")

#Determinamos el valor gastado menusalmente en transporte diferente al TM
if answer_transporte == "Si":
    precio_transporte = int(input("Ingrese el valor promedio mensual del precio de transporte diferente al TM: "))
elif answer_transporte == "No":
    precio_transporte = 0
else:
    print("Ingrese una respuesta Si/No: ")

Transporte = int(transporte(answer_transporte, workdays, tm, precio_transporte)) #Determinamos el total gastado en transporte

Mercado = int(input("Ingrese su presupuesto para mercado: ")) #Valor mensual gasrado en mercado

Entretenimiento = int(input("Ingrese su presupuesto para entretenimiento (Salidas/Comidas/Cine/Fiestas/etc): ")) #Valor que se gasta en otras actividades diferentes

Arriendo = Ingresos - (Transporte + Mercado + Entretenimiento) #Valor que le queda para el arriendo después de calcular los demás gastos

print("Según tus ingresos y gastos mensuales, puedes vivir en las siguientes localidades: ")

#Determinamos las localidades donde puede vivir según el valor de "Arriendo"
if Arriendo > min_barrios_unidos and Arriendo < max_barrios_unidos:
    print("Barrios unidos")

if Arriendo > min_suba and Arriendo < max_suba:
    print("Suba")

if Arriendo > min_bosa and Arriendo < max_bosa:
    print("Bosa")

if Arriendo > min_engativa and Arriendo < max_engativa:
    print("Engativa")

if Arriendo > min_teusaquillo and Arriendo < max_teusaquillo:
    print("Teusaquillo")

if Arriendo > min_usaquen and Arriendo < max_usaquen:
    print("Usaquen")

if Arriendo > min_fontibon and Arriendo < max_fontibon:
    print("Fontibon")

if Arriendo > min_kennedy and Arriendo < max_kennedy:
    print("Kennedy")

if Arriendo > min_puente_aranda and Arriendo < max_puente_aranda:
    print("Puente Aranda")

if Arriendo > min_san_cristobal and Arriendo < max_san_cristobal:
    print("San Cristobal")

if Arriendo > min_santa_fe and Arriendo < max_santa_fe:
    print("Santa Fe")