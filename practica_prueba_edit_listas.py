import os
os.system("cls")

def operacion ():
    #print(f"Asi esta la lista"[cosas])
    print ("¿Que deseas? Agregar o sacar algo de esta lista")
    print("1-AGREGAR")
    print ("2-SACAR")
    opcion= input("Cual es tu opcion: ")
    opcion= int(opcion)
    if opcion == 1:
       agregar = input("Escribe lo que quieres agregar:")
       cosas.append(agregar)
    elif opcion == 2:
        sacar = input ("Escribe el dato que quieras sacar con el indice, contando desde el 0:  ")
        sacar = int(sacar)
        cosas.pop(sacar)
    else: 
        print("La opcion no es correcta")
    print(f"Su lista quedo de esta manera{cosas}")   

print ("Hola como estas? ")
print("Esta es nuestra lista: ")
cosas = [1, 'Hola', 2, 5 ,'Gato', "Perro"]
print (cosas)

operacion()
"""print ("¿Que deseas? Agregar o sacar algo de esta lista")
print("1-AGREGAR")
print ("2-SACAR")
opcion= input("Cual es tu opcion: ")
opcion= int(opcion)"""


 


print(f"Su lista quedo de esta manera{cosas}")  
print("¿Tu, quieres seguir agregando o quitando datos de esta lista?")
print("1- SI")
print("2 -NO")
choice = input("Eliga la opcion que deseee: ")
choice = int(choice)
if choice == 1:
     operacion()
if choice == 2:
    print ("Bueno maestro esta todo de diez, vaya con dios!")



