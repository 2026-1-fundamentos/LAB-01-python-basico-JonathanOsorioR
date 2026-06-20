"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    dic = {}
    total = []
    ruta = r"C:\fundamentos\Laboratorios\LAB-01-python-basico-JonathanOsorioR\files\input\data.csv"
    with open(ruta, "r") as data:
        for row in data:
            row = row.split('\t')[0:2]
            dic[row[0]] = dic.get(row[0], 0) + 1
            total.append(row)
    total.sort()
    lista = sorted(list(dic.items()))
    print(f"unicos:{lista}")
    print(f"total:{total}")
    #lista = pregunta_02()
    inicio = 0
    final= lista[0][1]
    respuesta = []
    maximo = 0
    minimo = 0

    for i in range(len(lista)):

        minimo = min(total[inicio:final])[1]
        maximo = max(total[inicio:final])[1]

        if final<len(total):
            inicio = final
            final += int(lista[i+1][1])
            print(inicio)
            print(final)

        respuesta.append((lista[i][0],int(maximo),int(minimo)))

    return respuesta

print(pregunta_05())
    
    