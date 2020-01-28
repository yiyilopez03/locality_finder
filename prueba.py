import numpy as np
import pandas as pd
from funciones import transporte, completar

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
print(Transporte)

Mercado = int(input("Ingrese su presupuesto para mercado: "))

Entretenimiento = int(input("Ingrese su presupuesto para entretenimiento (Salidas/Comidas/Cine/Fiestas/etc): "))

Arriendo = Ingresos - (Transporte + Mercado + Entretenimiento)