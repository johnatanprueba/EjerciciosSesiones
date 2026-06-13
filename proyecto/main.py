import menu
import moduloCuentas


opt = menu.menuPrincipal()
while(opt!=5):
    if opt == 1:
        numeroDoc,nombre = menu.menuCrearCuenta()
        moduloCuentas.crearCuenta(numeroDoc,nombre)

    if(opt == 2):
        print("consignar dinero")
    if(opt == 3):
        print("Retirar dinero")
    if(opt == 4):
        print("Pagar servicios")
    
    opt = menu.menuPrincipal()

