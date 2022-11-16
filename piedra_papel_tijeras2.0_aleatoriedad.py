import os
import random

os.system("cls")

juego = ["piedra", "papel", "tijeras"]
computadora = random.choice(juego)

def computadora_gana():
    print("¡Gana la computadora!")
    print(f"La computadora eligió {computadora}")

while True:
    jugador = input("Elige tu opción: piedra, papel o tijeras: ")

    if jugador not in juego:
        print("¡No es una opción correcta!")
        continue
    if computadora == "piedra" and jugador == "tijeras":
        computadora_gana()
    elif computadora == "papel" and jugador == "piedra":
        computadora_gana()
    elif computadora == "tijeras" and jugador == "papel":
        computadora_gana()
    elif computadora == jugador:
        print("¡Nadie gana! :(")
        print(f"La computadora eligió {computadora}")
    else:
        print("¡Felicidades, le ganaste a la computadora!")
        print(f"La computadora eligió {computadora}")
        break