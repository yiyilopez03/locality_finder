import numpy as np
import pandas as pd

#Esta función la utilizamos en main.py para calcular el valor del transporte
def transporte(answer_transporte, workdays, tm, precio_transporte):
    tm_price = (tm * 2200) * workdays
    answer = answer_transporte
    if answer == "Si":
        transport = tm_price + precio_transporte
    elif answer == "No":
        transport = tm_price
    return transport

#Función utilizada en ambos códigos para extraer solo la columna de los precios en la base de datos
def precio (X):
    price = (X.iloc[:, 2])
    return price

#Función que creamos con sklearn para completar datos faltantes, pero se descarto al presentar dificultades con algunas de ellas
def completar (X):
    from sklearn.impute import SimpleImputer
    Xi = X.copy()
    imputer_num = SimpleImputer(strategy = "mean")
    a = Xi.columns[np.sum(Xi.isna())> 0]
    imputer_num.fit(Xi[a])
    Xi[a] = imputer_num.transform(Xi[a])
    Xi.info()
    return Xi