import json
import moduloUtil
def crearCuenta(numeroDoc,nombre):
    dtoCuenta = {"numeroDoc":numeroDoc,"nombre":nombre}
    listaCuentas = getListaCuentas()
    dtoCuenta["id"] = moduloUtil.getMaxIdListaCuenta(listaCuentas)
    dtoCuenta["password"] = moduloUtil.generatePassword(dtoCuenta)
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
    
