"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    dic = {}
    ruta = r"C:\fundamentos\Laboratorios\LAB-01-python-basico-JonathanOsorioR\files\input\data.csv"
    with open(ruta, "r") as data:
        for i in data:
            i = i.strip("\n").split('\t')[4].split(",")
            print(i)
            for j in i:
                z = j.split(":")
            
                if z[0] not in dic:
                    dic[z[0]] = [z[1],z[1]] 

                else:
                    dic[z[0]] = [min(int(z[1]),int(dic[z[0]][0])),max(int(z[1]),int(dic[z[0]][1]))]

        

    respuesta = [tuple([i[0],i[1][0],i[1][1]]) for i in sorted(list(dic.items()))]

    return respuesta
print(pregunta_06())