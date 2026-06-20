"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    ruta = r"C:\fundamentos\Laboratorios\LAB-01-python-basico-JonathanOsorioR\files\input\data.csv"
    with open(ruta, "r") as data:
        suma = sum(int(row.split('\t')[1]) for row in data)

    return suma
            
print(pregunta_01())