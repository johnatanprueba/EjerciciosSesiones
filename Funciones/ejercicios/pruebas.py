miVariableGlobal = "Hola global"
def funcionCambiarGlobal():
    global miVariableGlobal
    miVariableGlobal = "global cambiada"

funcionCambiarGlobal()
print(miVariableGlobal)#global cambiada

