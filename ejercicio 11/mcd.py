

#  Versión iterativa del algoritmo de Euclides para el cálculo del mcd de dos números enteros

def mcd_iterativo(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

#  Versión iterativa que calcula el mcd haciendo solo sumas o restas

def mcd_iterativo_suma_resta(a, b):
    a = abs(a)
    b = abs(b)
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
