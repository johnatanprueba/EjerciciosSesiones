menu = "1.Crear cuenta bancaria\n"
menu+= "2.Consignar dinero a una cuenta\n"
menu+= "3.Retirar dinero\n"
menu+= "4.Pagar servicios\n"
menu+= "5.Mostar movimientos bancarios\n"

def menuPrincipal():
    opt = int(input(menu))
    return opt

def menuCrearCuenta():
    numeroDocumento = input("Digite numero documento\n")
    nombre = input("Digite nombre\n")
    return numeroDocumento,nombre
    


