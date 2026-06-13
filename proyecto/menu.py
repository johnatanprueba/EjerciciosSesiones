import moduloCuentas

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
    contrasenia = input("Digite contraseña\n")
    return numeroDocumento,nombre,contrasenia

def menuConsignarDinero():
    while True:
        idCuenta = int(input("Digite el id de la cuenta a la que desea consignar\n"))
        valor = float(input("Digite el valor a consignar\n"))
        cuenta = moduloCuentas.getCuentaById(idCuenta)
        if valor < 0:
            print("El valor a consignar no puede ser negativo")
            sel = input("Desea volver a ingresar el valor? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                break
        elif cuenta is None:
            print("El id de cuenta no existe")
            sel = input("Desea volver a ingresar el id de cuenta? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                break
        else:   
            return idCuenta,valor
    return None,None    

def menuRetirarDinero(idCuenta):
    while True:
        valor = float(input("Digite el valor a retirar\n"))
        cuenta = moduloCuentas.getCuentaById(idCuenta)
        if valor < 0:
            print("El valor a retirar no puede ser negativo")
            sel = input("Desea volver a ingresar el valor? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                break
        elif cuenta is None:
            print("El id de cuenta no existe")
            sel = input("Desea volver a ingresar el id de cuenta? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                break
        elif valor > cuenta.get("saldo",0):
            print("El valor a retirar no puede ser mayor al saldo de la cuenta")
            sel = input("Desea volver a ingresar el valor? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                break
        else:
            return idCuenta,valor
    return None,None
    

def menuLogueo():
    idCuenta = None
    while True:
        idCuenta = int(input("Digite el id de la cuenta a la que desea retirar\n"))
        contrasenia = input("Digite contraseña\n")
        cuenta = moduloCuentas.getCuentaById(idCuenta)
        if cuenta is not None and cuenta.get("password") == contrasenia:
            break
        else:
            print("El id de cuenta o contraseña son incorrectos")
            sel = input("Desea volver a ingresar el id de cuenta y contraseña? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                idCuenta = None              
                break
    return idCuenta 