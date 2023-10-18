import random

def adivina_el_numero(x):
    
    print("=================================")
    print(f"Elije un numero entre 0 y {x}")
    print("=================================")
    
    limite_inf = 1
    limite_sup = x
    respuesta = ""
    
    while respuesta != "correcto":
        if limite_inf != limite_sup:
            prediccion = random.randint(limite_inf, limite_sup)
        else:
            prediccion = limite_sup

        respuesta = input(f"Mi prediccion es {prediccion}. si es muy alta ingresa (Alta), si es muy baja ingresa (Baja) y si es correcta ingresa (Correcto)").lower()
        
        if respuesta == "alta":
            limite_inf = prediccion + 1
        elif respuesta == "baja":
            limite_sup = prediccion - 1
    print(f"Tu numero es: {prediccion}")

while True:
        try:
            maximo = int(input("Elige el numero maximo: "))
            adivina_el_numero(maximo)
        except ValueError:
            print("Por favor, ingresa un número válido.")