import random
import time 


def busqueda_ingenua(list, target):
    for idx in range(len(list)):
        if list[idx] == target:
            return idx
    return -1

def busqueda_binaria(list, target, limite_inf=None, limite_sup=None):
    if limite_inf is None:
        limite_inf = 0
    if limite_sup is None:
        limite_sup = len(list)-1
    if limite_sup < limite_inf:
        return -1

    medio = (limite_inf + limite_sup) // 2

    if list[medio] == target:
        return medio
    elif target < list[medio]:
        return busqueda_binaria(list, target, limite_inf, medio-1)
    else:
        return busqueda_binaria(list, target, medio+1, limite_sup)


if __name__=='__main__':
    mi_lista = [
    "Juan",
    "María",
    "Carlos",
    "Ana",
    "Luis",
    "Laura",
    "Pedro",
    "Sofía",
    "Miguel",
    "Isabel",
    "Alejandro",
    "Elena",
    "Javier",
    "Carmen",
    "Roberto",
    "Valentina",
    "Andrés",
    "Paula",
    "Ricardo",
    "Natalia",
    "Diego",
    "Raquel",
    "José",
    "Beatriz",
    "Felipe",
    "Daniela",
    "Antonio",
    "Patricia",
    "Gustavo",
    "Adriana",
    "Fernando",
    "Lucía",
    "Manuel",
    "Camila",
    "Rodrigo",
    "Verónica",
    "Gabriel",
    "Teresa",
    "Rafael",
    "Luisa",
    "Santiago",
    "Eva",
    "Francisco",
    "Valeria",
    "Esteban",
    "Martha",
    "Ángel",
    "Rosa"
]
    print(busqueda_binaria(mi_lista, "Verónica"))