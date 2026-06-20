"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    dic = {}
    ruta = r"C:\fundamentos\Laboratorios\LAB-01-python-basico-JonathanOsorioR\files\input\data.csv"
    with open(ruta, "r") as data:
   
        for i in data:
            i = i.split("\t")[0:2]
            if i[0] in dic:
                dic[i[0]]+=int(i[1])

            else:
                dic[i[0]]=int(i[1])

    lista = sorted(list(dic.items()))
    return lista
print(pregunta_03())
