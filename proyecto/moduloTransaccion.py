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

def getTransaccionesByIdCuenta(idCuenta):
    listaTransacciones = getTransacciones()
    listaTransaccionesCuenta = []
    for transaccion in listaTransacciones:
        if transaccion["idCuenta"] == idCuenta:
            listaTransaccionesCuenta.append(transaccion)
    
    if len(listaTransaccionesCuenta) > 0:
        listaTransaccionesCuenta.sort(key=lambda x: x["fecha"],reverse=True)
    return listaTransaccionesCuenta