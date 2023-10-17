import random


def adivina_el_numero(x):
    
    print("=================================")
    print(f"Adivina el numero entre 0 y {x}")
    print("=================================")
    
    while True:
        try:
            x = int(input("Elige el numero maximo: "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    numero = random.randint(0, x)
    prediccion = -1

    while prediccion != numero:
        try:
            prediccion = int(input("¿QUÉ NÚMERO ES?: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if prediccion < numero:
            print(f"El numero es mayor a {prediccion}")
        elif prediccion > numero:
            print(f"El numero es menor que {prediccion}")
    
    print(f"Felicitaciones adivinaste el numero {numero}")
    
adivina_el_numero(10)
