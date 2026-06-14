import json
import moduloUtil
import moduloTransaccion
from datetime import datetime
def crearCuenta(numeroDoc,nombre,contrasenia):
    dtoCuenta = {"numeroDoc":numeroDoc,"nombre":nombre,"password":contrasenia,"saldo":0}
    listaCuentas = getListaCuentas()
    dtoCuenta["id"] = moduloUtil.getMaxIdListaCuenta(listaCuentas)
    #dtoCuenta["password"] = moduloUtil.generatePassword(dtoCuenta)
    listaCuentas.append(dtoCuenta)
    
    with open("cuenta.json","w") as archivoCuenta:
        archivoCuenta = json.dump(listaCuentas,archivoCuenta,indent=4)

def getListaCuentas():
    listaCuenta = []
    try:
        with open("cuenta.json","r") as archivoCuenta:
            listaCuenta = json.load(archivoCuenta)
    except FileNotFoundError as e:
        print("No se ha creado el archivo cuentas.json")
    return listaCuenta

def consignarDinero(idCuenta,valor):
    listaCuentas = getListaCuentas()
    for cuenta in listaCuentas:
        if cuenta["id"] == idCuenta:
            cuenta["saldo"] = cuenta.get("saldo",0) + valor
            break
    with open("cuenta.json","w") as archivoCuenta:
        archivoCuenta = json.dump(listaCuentas,archivoCuenta,indent=4)
    moduloUtil.mostrarTRansaccion(idCuenta,"Consignacion",valor)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    moduloTransaccion.crearTransaccion(idCuenta,"Consignacion",valor,fecha)

def retirarDinero(idCuenta,valor):
    listaCuentas = getListaCuentas()
    for cuenta in listaCuentas:
        if cuenta["id"] == idCuenta:
            cuenta["saldo"] = cuenta.get("saldo",0) - valor
            break
    with open("cuenta.json","w") as archivoCuenta:
        archivoCuenta = json.dump(listaCuentas,archivoCuenta,indent=4)
    moduloUtil.mostrarTRansaccion(idCuenta,"Retiro",valor)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    moduloTransaccion.crearTransaccion(idCuenta,"Retiro",valor,fecha)

def getCuentaById(idCuenta):
    listaCuentas = getListaCuentas()
    for cuenta in listaCuentas:
        if cuenta["id"] == idCuenta:
            return cuenta
    return None

def pagarServicio(idCuenta,valorServicio,strServicio):
    listaCuentas = getListaCuentas()
    for cuenta in listaCuentas:
        if cuenta["id"] == idCuenta:
            cuenta["saldo"] = cuenta.get("saldo",0) - valorServicio
            break
    with open("cuenta.json","w") as archivoCuenta:
        archivoCuenta = json.dump(listaCuentas,archivoCuenta,indent=4)
    moduloUtil.mostrarTRansaccion(idCuenta,"Pago Servicio "+strServicio,valorServicio)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    moduloTransaccion.crearTransaccion(idCuenta,"Pago Servicio " + strServicio,valorServicio,fecha)

    
