import menu
import moduloCuentas
import moduloTransaccion

opt = menu.menuPrincipal()
while(opt!=0):
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
        idCuenta = menu.menuLogueo()
        if idCuenta is not None:
            valorServicio,strServicio = menu.menuPagarServicios(idCuenta)
            if valorServicio is not None and strServicio is not None:
                moduloCuentas.pagarServicio(idCuenta,valorServicio,strServicio)
    if(opt == 5):
        idCuenta = menu.menuLogueo()
        if idCuenta is not None:
            transacciones = moduloTransaccion.getTransaccionesByIdCuenta(idCuenta)
            if transacciones is not None and len(transacciones)>0:
                print("Movimientos bancarios:")
                for transaccion in transacciones:
                    print(f"{transaccion['tipoTransaccion']} - {transaccion['monto']} - {transaccion['fecha']}")
            else:
                print("No se han encontrado movimientos bancarios para esta cuenta")
    
    opt = menu.menuPrincipal()

