import os
os.system("cls")

i=0

while (i< 5): #esta condicion se cumpla
    if i == 3: # si quiero que corte hasta el numero que quiero se usa un if y el break
         i= i+ 1 # con esto saltamos el 3, suma 1 y pasa a seguir el codigo
         continue #saltar una vuelta del ciclo
         #break para cortar el ciclo, frenarlo
    print(f"Hola en este momento i vale {i}")#este codigo se repite
    i= i+ 1  #codigo que altera la condicion hasta donde quiere que corte y no sea bucle infinito
