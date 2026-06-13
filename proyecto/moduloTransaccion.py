import json

def getTransacciones():
    listaTransacciones = []
    try:
        with open("transaccion.json","r") as archivoTransaccion:
            listaTransacciones = json.load(archivoTransaccion)
    except FileNotFoundError as e:
        print("No se ha creado el archivo transaccion.json")
    return listaTransacciones

def crearTransaccion(idCuenta,tipoTransaccion,monto,fecha):
    dtoTransaccion = {"idCuenta":idCuenta,"tipoTransaccion":tipoTransaccion,"monto":monto,"fecha":fecha}
    listaTransacciones = getTransacciones()
    listaTransacciones.append(dtoTransaccion)
    with open("transaccion.json","w") as archivoTransaccion:
        archivoTransaccion = json.dump(listaTransacciones,archivoTransaccion,indent=4)