import numpy as np
import pandas as pd

def transporte(answer_transporte, workdays, tm, precio_transporte):
    tm_price = (tm * 2200) * workdays
    answer = answer_transporte
    if answer == "Si":
        transport = tm_price + precio_transporte
    elif answer == "No":
        transport = tm_price
    return transport

def completar (X):
    from sklearn.impute import SimpleImputer
    Xi = X.copy()
    imputer_num = SimpleImputer(strategy = "median")
    a = Xi.columns[np.sum(Xi.isna())> 0]
    imputer_num.fit(Xi[a])
    Xi[a] = imputer_num.transform(Xi[a])
    Xi.info()
    return Xi