def menu(a,b):
    print("Menu")
    print(a)
    print(b)

    while(True):
        numeroSeleccionado = input("Ingresa un numero de opcion")
        if (numeroSeleccionado == "1"):
            print("Gracias")
            return numeroSeleccionado
        
        elif(numeroSeleccionado == "2"):
            print("Gracias vuelva a comprar pronto")
            return numeroSeleccionado
        else:
            print("seleccione una opcion valida")