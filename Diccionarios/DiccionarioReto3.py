productos = { 
'Menta':{'costo':40, 'precio':300, 'cantidadDisponible':10}, 
'Chocorramo':{'costo':700, 'precio':1000, 'cantidadDisponible':12}
}

for k,v in productos.items():
    cantidadDisponible = v.get("cantidadDisponible")
    precio = v.get("precio")
    costo = v.get("costo")
    valorUnitario = precio-costo
    valorTotal = valorUnitario*cantidadDisponible
    print(k+" total ganado:",valorTotal)