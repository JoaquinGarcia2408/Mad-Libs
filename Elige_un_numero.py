import random

def adivina_el_numero(x):
    print("=================================")
    print(f"Elije un número entre 0 y {x}")
    print("=================================")

    limite_inf = 1
    limite_sup = x
    respuesta = ""

    while respuesta.lower() != "correcto":
        if limite_inf != limite_sup:
            prediccion = random.randint(limite_inf, limite_sup)
        else:
            prediccion = limite_sup

        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa 'Alta'; si es muy baja, ingresa 'Baja'; y si es correcta, ingresa 'Correcto': ").lower()

        if respuesta == "alta":
            limite_sup = prediccion - 1
        elif respuesta == "baja":
            limite_inf = prediccion + 1
        elif respuesta != "correcto":
            print("Por favor, ingresa 'Alta', 'Baja' o 'Correcto'.")

    print(f"Tu número es: {prediccion}")

while True:
    try:
        maximo = int(input("Elige el número máximo: "))
        adivina_el_numero(maximo)
    except ValueError:
        print("Por favor, ingresa un número válido.")