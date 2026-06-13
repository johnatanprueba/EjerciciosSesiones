productos = { 'Menta':{'costo':40, 'precio':300, 'cantidadDisponible':10}
             , 'Chocorramo':{'precio':1000, 'cantidadDisponible':12}}
totalProductos = 0
listProductosKey = productos.keys()
for producto,info in productos.items():
    cantidad = info.get("cantidadDisponible")
    totalProductos+=cantidad
    print(producto+" hay ",cantidad," unidades disponibles")
print("Número total de productos de la tienda:",totalProductos)
