def getMaxIdListaCuenta(listCuentas):
    idGenerate = 1
    if len(listCuentas)>0:
        cuenta = max(listCuentas,key=lambda cuenta:cuenta["id"])
        idGenerate = cuenta["id"]+1
    return idGenerate

def generatePassword(dtoCuenta):
    return dtoCuenta["numeroDoc"]+dtoCuenta["nombre"]

def mostrarTRansaccion(monto,tipoTransaccion):
    print(f"Se ha realizado una transaccion de tipo {tipoTransaccion} por un monto de {monto}")

