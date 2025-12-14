#PROYECTO DE ADIVINAR EL NUMERO QUE ESTOY PENSANDO
#1.- TIENE 8 INTENTOS
#2.- OPCION 1 : SI EL NUMERO INGRESADO ES MAYOR QUE 100 O MENOR DE 1 O 0 DECIRLE QUE EL NUMEOR INGHRESAOD NO ESTA DENTRO DEL RANGO
#3.- OPCION 2 : SI EL NUMERO INGRESADO ES MENOR AL QUE ESCOGIO EL PROGRAMA QUE LE DIGA QUE EL NUMERO INGRESADO ES ERRONIO Y LO MISMO SI ES MAYOR
#4.- OPCION 3 : SI ACERTAQUE LO FELICITE Y QUE DIGA "RAYOS LO ADIVINASTE {NAME} FELICITACIONES"

import random

print("HOLA! BIENVENIDO AL JUEGO DE ADIVINA EL NUMERO")

nombre = input("DIME CÓMO TE LLAMAS: ").upper()
print(f"HOLA {nombre}! BIEN, COMENCEMOS.")
print("ESTOY PENSANDO EN UN NÚMERO DEL 1 AL 100...")

numero_intentos = 0
numero_random = random.randint(1, 100)

while numero_intentos < 8:

    numero = input("DIGITE EL NÚMERO: ")

    if not numero.isdigit():
        print("⚠ ERROR: Debes ingresar únicamente números.")
        continue

    numero = int(numero)
    numero_intentos += 1

    if numero < 1 or numero > 100:
        print("⚠ El número ingresado está fuera del rango (1–100). Intenta nuevamente.")
        continue

    if numero == numero_random:
        print(f"🎉 RAYOS LO ADIVINASTE {nombre}! FELICITACIONES.")
        print(f"Lo lograste en {numero_intentos} intentos.")
        break

    elif numero < numero_random:
        print(f"❌ El número es demasiado BAJO. Te quedan {8 - numero_intentos} intentos.")

    elif numero > numero_random:
        print(f"❌ El número es demasiado ALTO. Te quedan {8 - numero_intentos} intentos.")

    if numero_intentos == 8:
        print(f"\n😢 PERDISTE, {nombre}. Solo tenías 8 intentos.")
        print(f"El número era: {numero_random}")
