from typing import List, Tuple

class PALABRA:
    def __init__(self, palabra:str, ant:int, sig:int):
        self.palabra = palabra
        self.ant = ant
        self.sig = sig
        
def buscar_palabras_letra_iter(diccionario: List[PALABRA], letra: str) -> List[str]:
    resultado = []
    i = 0
    while i < len(diccionario):
        if diccionario[i].palabra[0] == letra:
            resultado.append(diccionario[i].palabra)
        i = diccionario[i].sig
    return resultado

def agregar_palabra_iter(diccionario: List[PALABRA], palabra:str) -> List[PALABRA]:
    if len(diccionario) == 0:
        nueva_palabra = PALABRA(palabra, 0, 0)
        diccionario.append(nueva_palabra)
        return diccionario
    else:
        i = 0
        while i < len(diccionario):
            if diccionario[i].palabra > palabra:
                nueva_palabra = PALABRA(palabra, diccionario[i-1].sig, i)
                diccionario[i-1].sig = len(diccionario)
                diccionario.insert(i, nueva_palabra)
                return diccionario
            i = diccionario[i].sig
        nueva_palabra = PALABRA(palabra, len(diccionario)-1, 0)
        diccionario[len(diccionario)-1].sig = len(diccionario)
        diccionario.append(nueva_palabra)
        return diccionario
