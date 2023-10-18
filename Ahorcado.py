import random
import string

from palabras import palabras_español
from diagramas import vidas_diccionario_visual


def obtener_palabra(lista_palabras):
    la_palabra = random.choice(palabras_español)
    return la_palabra.upper()


def ahorcado():
    print("=================================")
    print("   Vamos a jugar al ahorcado!")
    print("=================================")

    palabra = obtener_palabra(palabras_español)

    letras_por_adivinar = set(palabra)
    
    # Verifica si hay al menos una letra por adivinar
    if not letras_por_adivinar:
        print("Error: No hay palabra para adivinar.")
        return
    
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()

    vidas = 7

    while letras_por_adivinar and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        palabra_lista = [letra if letra in letras_adivinadas else "-" for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra:").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("")
            else:
                vidas = vidas - 1
                print(f"\n La letra {letra_usuario} no está en la palabra")
        elif letra_usuario in letras_adivinadas:
            print("\n Ya dijiste esa letra, elige otra")
        else:
            print("Esta letra no es válida")
    
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"PERDISTE, la palabra era {palabra}")
    else:
        print(f"¡ADIVINASTE LA PALABRA: {palabra}!")

ahorcado()