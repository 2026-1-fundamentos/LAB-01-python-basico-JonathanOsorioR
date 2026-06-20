"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    ruta = os.path.join("files", "input", "data.csv")

    dic = {}
    with open(ruta, "r") as data:
        for row in data:
            row = row.strip("\n").split("\t")
            row = [row[0],row[4].split(",")]

            for i in row[1]:
                i = i.split(":")
                if row[0] in dic:
                    dic[row[0]] += int(i[1])
                else:
                    dic[row[0]] = int(i[1])
    dic = dict(sorted(dic.items()))
    return dic
