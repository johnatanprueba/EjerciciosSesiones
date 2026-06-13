import menu
import moduloCuentas


opt = menu.menuPrincipal()
while(opt!=5):
    if opt == 1:
        numeroDoc,nombre,contrasenia = menu.menuCrearCuenta()
        moduloCuentas.crearCuenta(numeroDoc,nombre,contrasenia)

    if(opt == 2):
        idCuenta,valor = menu.menuConsignarDinero()
        moduloCuentas.consignarDinero(idCuenta,valor)
    if(opt == 3):
        print("Retirar dinero")
    if(opt == 4):
        print("Pagar servicios")
    
    opt = menu.menuPrincipal()

