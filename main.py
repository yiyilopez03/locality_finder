import numpy as np
import pandas as pd
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

Ingresos = int(input("Ingrese sus ingresos mensuales: "))

workdays = int(input("Ingrese el número de días que trabaja/estudia a la semana: "))
tm = int(input("Ingrese el número de veces que usa TM en el día: "))

answer_transporte = " "
while answer_transporte != "Si" or "No":
    answer_transporte = str(input("¿Usa otro medio de transporte diferente a TM?: "))
    print("Digíte una respuesta Si/No")
    if answer_transporte == "Si" or "No":
        break

if answer_transporte == "Si":
    precio_transporte = int(input("Ingrese el valor promedio mensual del precio de transporte diferente al TM: "))
elif answer_transporte == "No":
    precio_transporte = 0
else:
    print("Ingrese una respuesta Si/No: ")

Transporte = int(transporte(answer_transporte, workdays, tm, precio_transporte))

Mercado = int(input("Ingrese su presupuesto para mercado: "))

Entretenimiento = int(input("Ingrese su presupuesto para entretenimiento (Salidas/Comidas/Cine/Fiestas/etc): "))

Arriendo = Ingresos - (Transporte + Mercado + Entretenimiento)

print("Según tus ingresos y gastos mensuales, puedes vivir en las siguientes localidades: ")

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