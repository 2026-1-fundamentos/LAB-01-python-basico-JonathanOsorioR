"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    ruta = r"C:\fundamentos\Laboratorios\LAB-01-python-basico-JonathanOsorioR\files\input\data.csv"
    dic = {}
    with open(ruta, "r") as data:
        for row in data:
            row = row.split("\t")
            row = [row[1],row[3].split(",")]
            for i in row[1]:
                if i in dic:
                    dic[i] += int(row[0])
                else:
                    dic[i] = int(row[0])
    ordenado = dict(sorted(dic.items()))
    return ordenado

print(pregunta_11())
