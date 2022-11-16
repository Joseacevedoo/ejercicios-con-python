import enum
import os
os.system("cls")
import random

pc_choice = ["Piedra","papel","tijeras"]

eleccion =input("Elige tu opcion: (piedra,papel o tijeras) ")


eleccion = random.choice(pc_choice)


if eleccion == "papel":
    print("Computadora elige Tijeras. Gana la computadora :) ")
elif eleccion =="piedra":
    print("Computadora elige Papel. Gana la computadora :)")
elif eleccion == "tijeras":
    print("Computadora elige Piedra. Gana la computadora :)")
else:
    print("Elige una opcion corecta")

