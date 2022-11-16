#import os y os.system es para limpiar la pantalla cada vez que se ejecuta el programa

import os
os.system("cls")

def conversor(moneda):   #se usa una funcion para acortar el codigo, se le asigna un parametro (una variable q uno puede cambiar)
    pesos = int(input("¿Cuantos pesos tienes?"))
    dolares = pesos / moneda     #aca se pone el parametro definido entre () 
    return dolares

USD = 1
ARS = 290
COP = 4600
MXN = 20

print("¡Bienvenido al conversor de moneda definitivo!")
print("Elige una de las siguientes opciones de conversion: ")
print("1 - Pesos argentinos a dolares estadounidenses")
print("2 - Pesos colombianos a dolares estadounidenses")
print("3 - Pesos mexicanos a dolares estadounidenses")
opcion = input("¿Cual es tu opcion?: ")
#casteo se cambia opcion q es un str a entero para guardar el valor
opcion = int(opcion)

if opcion == 1:
    dolares = conversor (ARS)
    print(f"Tienes ${dolares} dolares")   #cuando se invoca la funcion en los () se coloca la constante definida en el codigo
elif opcion == 2:
    dolares =conversor(COP)
    print(f"Tienes ${dolares} dolares") 
elif opcion == 3:
    dolares = conversor (MXN)
    print(f"Tienes ${dolares} dolares") 
else:
    print("Escribe una opcion correcta! ")



