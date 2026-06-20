"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    ruta = r"C:\fundamentos\Laboratorios\LAB-01-python-basico-JonathanOsorioR\files\input\data.csv"
    lista = []
    with open(ruta, "r") as data:
        for row in data:
            row = row.strip("\n").split("\t")
            row[3] = row[3].split(",")
            row[4] = row[4].split(",")
            lista.append((row[0],len(row[3]),len(row[4])))
    return lista

print(pregunta_10())