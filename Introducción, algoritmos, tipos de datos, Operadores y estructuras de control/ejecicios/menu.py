saldo = 1000000
sw = 1
while sw !=0:
    print("Muenu\n1.consultar saldo\n2.retirar dinero\n3.depositar dinero\n4.salir")
    opcion = int(input())

    if opcion == 1:
        print("El saaldo es:",saldo)
    elif opcion == 2:
        print("Digite el monto a retirar")
        montoRetirar = float(input())
        if montoRetirar>saldo:
            print("No puede retirar mas del saldo")
        else:
            saldo = saldo - montoRetirar
    elif opcion == 3:
        print("Digite el monto a infresar")
        montoIngresar =  float(input())
        saldo = saldo +montoIngresar
    elif opcion == 4:
        sw = 0
    else:
         print("Digite una opcion valida")
