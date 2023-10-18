import random

def jugar():
    usuario = input("Elige entre piedra, papel o tijera. \n")
    computadora = random.choice(["piedra", "papel", "tijera"])
    print(f"Computadora: {computadora}")

    if usuario == computadora:
        return "Empate"
    if gano_el_juego(usuario, computadora):
        return "Ganaste"
    return "Perdiste"


def gano_el_juego(jugador, compu):
    if ((jugador == "piedra" and compu == "tijera")
        or (jugador == "tijera" and compu == "papel")
        or (jugador == "papel" and compu == "piedra")):
        return True
    else:
        return False

print(jugar())