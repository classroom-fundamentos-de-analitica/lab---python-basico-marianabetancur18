"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from collections import Counter
from datetime import datetime
from operator import index


csvfile= open("data.csv","r")


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    result = 0
    for row in csv.reader(csvfile, delimiter='\t'):
        result += int(row[1])

    return result


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    result=Counter()
    for row in csv.reader(csvfile, delimiter='\t'):
        result[row[0]]+=1

    result=sorted(result.items())

    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    result=Counter()
    for row in csv.reader(csvfile, delimiter='\t'):
        result[row[0]]+=int(row[1])

    result=sorted(result.items())
    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    result=Counter()
    for row in csv.reader(csvfile, delimiter='\t'):
        date= datetime.strptime(row[2],"%Y-%m-%S")

        result[str(date.month).zfill(2)]+=1

    result=sorted(result.items())

    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv') as file:

        data = file.readlines()
        data = [(x.strip().split('\t')[0:2]) for x in data]

        list_ = sorted((list(set([x[0] for x in data]))))
        result = list()

        for i in list_:
            valores = list()
            for j in data:
                if j[0] == i:
                    valores.append(int(j[1]))

            result.append((i, max(valores), min(valores)))

    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv') as file:

        data = file.readlines()
        data = [x.strip().split('\t')[-1] for x in data]
        data = ','.join(data).split(',')
        data = [x.split(':') for x in data]

        strings = sorted(list(set([x[0] for x in data])))
        result = list()

        for i in strings:
            valores = list()
            for j in data:
                if j[0] == i:
                    valores.append(int(j[1]))

            result.append((i, min(valores), max(valores)))

    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('data.csv') as file:

        data = file.readlines()
        data = [x.strip().split('\t')[0:2] for x in data]

        indx = sorted(list(set([int(x[1]) for x in data])))
        result = list()

        for i in indx:
            list_ = list()
            for j in data:
                if int(j[1]) == i:
                    list_.append(j[0])
            result.append((int(i), list_))

    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv') as file:

        data = file.readlines()
        data = [x.strip().split('\t')[0:2] for x in data]

        numbers = sorted(list(set([int(x[1]) for x in data])))
        result = list()

        for i in numbers:
            list_ = list()

            for j in data:
                if int(j[1]) == i:
                    list_.append(j[0])

            result.append((int(i), sorted(list(set(list_)))))

    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv') as file:
        data = file.readlines()
        data = [x.strip().split('\t')[-1] for x in data]
        data = ','.join(data).split(',')
        data = [x.split(':')[0] for x in data]

        strings = sorted(list(set(data)))
        result = dict()

        for i in strings:
            result[i] = data.count(i)

    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv') as file:
        data = file.readlines()
        data = [x.strip().split('\t') for x in data]

        for i in data:
            i.pop(1)
            i.pop(1)
            i[1] = len(i[1].split(','))
            i[2] = len(i[2].split(','))

        result = [tuple(x) for x in data]

    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv') as file:

        data = file.readlines()
        aux = data.copy()
        data = [x.strip().split('\t')[3] for x in data]
        data = ','.join(data).split(',')

        list_ = sorted(list(set(data)))
        aux = [x.strip().split('\t') for x in aux]
        result = dict()

        for i in list_:
            container = 0
            for j in aux:
                if i in j[3]:
                    container += int(j[1])
            result[i] = container

    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv') as file:

        data = file.readlines()
        data = [x.strip().split('\t') for x in data]

        list_aux = list()

        for i in data:
            for j in range(3):
                i.pop(1)
            i[1] = i[1].split(',')

        values = [x[1] for x in data]

        for j in values:
            list_ = sum([int(x.split(':').pop(1)) for x in j])
            list_aux.append(list_)

        for k in range(len(data)):
            data[k].append(list_aux[k])
            data[k].pop(1)

        l = [x[0] for x in data]
        l = sorted(list(set(l)))
        result = dict()

        for i in l:
            acum = 0
            for j in data:
                if j[0] == i:
                    acum += j[1]
            result[i] = acum

    return result
