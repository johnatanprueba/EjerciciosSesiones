from menu import *

print("Hola")

opcion1 = "Opción 1 Comprar Revista (digite 1 para comprar)" 
opcion2 = "Opción 2 No comprar (digite 2)"

numeroSeleccionado = menu(opcion1, opcion2)

if (numeroSeleccionado == '1'):
    print("Has elegido la opción 1: Comprar")
else:
    print("Has elegido la opcion 2: No comprar nada !")