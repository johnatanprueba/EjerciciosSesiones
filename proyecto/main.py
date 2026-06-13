import menu
import moduloCuentas


opt = menu.menuPrincipal()
while(opt!=5):
    if opt == 1:
        numeroDoc,nombre,contrasenia = menu.menuCrearCuenta()
        moduloCuentas.crearCuenta(numeroDoc,nombre,contrasenia)

    if(opt == 2):
        idCuenta,valor = menu.menuConsignarDinero()
        if idCuenta is not None and valor is not None:
            moduloCuentas.consignarDinero(idCuenta,valor)
    if(opt == 3):
        idCuenta = menu.menuLogueo()
        if idCuenta is not None:
            idCuenta,valor = menu.menuRetirarDinero(idCuenta)
            moduloCuentas.retirarDinero(idCuenta,valor)
    if(opt == 4):
        print("Pagar servicios")
    
    opt = menu.menuPrincipal()

