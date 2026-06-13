productos = { 'Menta':{'costo':40, 'precio':300, 'cantidadDisponible':10}
             , 'Chocorramo':{'precio':1000, 'cantidadDisponible':12}}
producto = input('¿Qué producto desea? ').title()
cantidad = int(input('¿Cuantos desea? '))

listProd = productos.keys()
if producto in listProd:
    dictPro = productos[producto]
    cant = dictPro.get("cantidadDisponible")
    pre = dictPro.get("precio")
    if cantidad>cant:
        print("No tenemos tantas "+producto)
    else:
        total = cantidad*pre
        print(cantidad,producto+"s valen $",total)
else:
     print("Lo siento, el producto", producto, "no está disponible.")
        
