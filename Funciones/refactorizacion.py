"""
Cajero automático    30 líneas de código
version 0.3
"""
denominaciones = [100000, 50000, 20000, 10000, 5000, 1000]
denominaciones.sort(reverse=True)
billetes = {}


print("Digite la cantidad que desea sacar de su cuenta:")


cantidad = int(input())
cantidadInicial= cantidad


def calcular_billetes(denominaciones, billetes, cantidad):
	for billete in denominaciones:
		cantidadBilletes = cantidad//billete
		cantidad = cantidad-cantidadBilletes*billete
		billetes[billete] = cantidadBilletes
	return billetes,cantidad

def imprimir(billetes,cantidadImp):
	outTxt = {}
	for billete in billetes:
		outTxt["Cantidad a revisar:"]=cantidadImp
		outTxt[str(billete)+":"] = billetes[billete]
	print(outTxt)
	
	


billetes, cantidad = calcular_billetes(denominaciones, {}, cantidad)
respuesta = {
    "Cantidad a revisar": cantidadInicial,
    "cien mil": billetes[100000],
    "Billetes de Cincuenta mil:": billetes[50000], 
    "Billetes de Veinte mil:": billetes[20000], 
    "Billetes de Diez mil:": billetes[10000], 
    "Billetes de cinco mil": billetes[5000], 
    "Monedas de mil": billetes[1000], 
    "Otras monedas": cantidad
    }


#print(respuesta)
imprimir(billetes,cantidadInicial)

denominaciones = [70000, 30000, 20000, 1000]
cantidad = cantidadInicial


billetes, cantidad = calcular_billetes(denominaciones, {}, cantidad)
respuesta = {
    "Cantidad a revisar": cantidadInicial,
    "Billetes de setenta mil": billetes[70000],
    "Billetes de Treinta mil:": billetes[30000], 
    "Billetes de Veinte mil:": billetes[20000],  
    "Monedas de mil": billetes[1000], 
    "Otras monedas": cantidad
    }


#print(respuesta)
imprimir(billetes,cantidadInicial)
