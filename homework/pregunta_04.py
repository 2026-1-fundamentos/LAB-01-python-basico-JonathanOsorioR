"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    ruta = r"C:\fundamentos\Laboratorios\LAB-01-python-basico-JonathanOsorioR\files\input\data.csv"
    dic = {}
    with open(ruta, "r") as data:

        for i in data:
            i = i.split('\t')[2].split("-")[1]
            if i in dic:
                dic[i]+=1

            else:
                dic[i]=1
    meses = sorted(list(dic.items()))
    return meses

print(pregunta_04())