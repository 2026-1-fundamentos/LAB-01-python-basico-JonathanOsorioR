"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    ruta = os.path.join("files", "input", "data.csv")

    dic = {}
    with open(ruta, "r") as data:
        for row in data:
            row = row.strip("\n").split("\t")[4].split(",")
            for i in row:
                i=i.split(":")
                #i[1] = int(i[1])
                if i[0] in dic:
                    dic[i[0]]+=1
                else:
                    dic[i[0]]=1
    return dic
