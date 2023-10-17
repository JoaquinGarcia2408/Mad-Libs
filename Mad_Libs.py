def obtener_input(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isalpha():
            return valor
        else:
            print("Por favor, ingresa una palabra válida (solo letras).")

adjetivo1 = obtener_input("Adjetivo: ")
plural_plu1 = obtener_input("Sustantivo en plural: ")
sustantivo1 = obtener_input("Sustantivo: ")
adjetivo2 = obtener_input("Adjetivo: ")
adjetivo3 = obtener_input("Adjetivo: ")
adjetivo4 = obtener_input("Adjetivo: ")
adjetivo5 = obtener_input("Adjetivo: ")
adjetivo6 = obtener_input("Adjetivo: ")
sustantivo3 = obtener_input("Sustantivo: ")
emoción = obtener_input("Una emocion: ")

madlibs = f"""Una vez, en un lejano y {adjetivo1} bosque,
un grupo de intrépidos {plural_plu1} descubrió un misterioso {sustantivo1}.
Este {sustantivo1} resultó ser un portal a un mundo {adjetivo2} y {adjetivo3},
lleno de criaturas {adjetivo4} y paisajes {adjetivo5}.
Los valientes exploradores se embarcaron en una emocionante aventura,
enfrentándose a desafíos {adjetivo6} y haciendo nuevos amigos.
Al final de su viaje, descubrieron el secreto de la {sustantivo3}, y sus corazones se llenaron de {emoción}."""

print(madlibs)