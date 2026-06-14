import moduloCuentas
import moduloUtil

menu = "1.Crear cuenta bancaria\n"
menu+= "2.Consignar dinero a una cuenta\n"
menu+= "3.Retirar dinero\n"
menu+= "4.Pagar servicios\n"
menu+= "5.Mostar movimientos bancarios\n"
menu+= "0.Salir\n"

menuServicios = "1.Energia\n"
menuServicios+= "2.Agua\n"
menuServicios+= "3.Gas\n"

dicServ = {
    "Energia":24000,
    "Agua":35000,  
    "Gas":50000
}

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
        idCuenta = int(input("Digite el id de la cuenta a la que desea realizar la transacción \n"))
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

def menuPagarServicios(idCuenta):
    valorServicio = None
    strServicio = None
    cuenta = moduloCuentas.getCuentaById(idCuenta)
    while True:
        opt = int(input(menuServicios))
        if opt == 1:
            print("Ha seleccionado pagar energia")
            valorServicio = dicServ.get("Energia")
            strServicio = "Energia"
        elif opt == 2:
            print("Ha seleccionado pagar agua")
            valorServicio = dicServ.get("Agua")
            strServicio = "Agua"
        elif opt == 3:
            print("Ha seleccionado pagar gas")
            valorServicio = dicServ.get("Gas")
            strServicio = "Gas"
        else:
            print("Opcion no valida")
            sel = input("Desea volver a seleccionar el servicio? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                valorServicio = None
                strServicio = None
                break

        if valorServicio > cuenta.get("saldo",0):
            print("El valor del servicio no puede ser mayor al saldo de la cuenta")
            sel = input("Desea volver a seleccionar el servicio? S/N\n")
            if sel.upper() == "S":
                continue
            else:
                valorServicio = None
                strServicio = None
                break
        else:
            break
    return valorServicio,strServicio


