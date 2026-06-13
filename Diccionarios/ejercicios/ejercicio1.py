def filtrar_inventario(productosDi):
    productosFiltrados = {}
    for k,v in productosDi.items():
        if v.get("precio")>50 and v.get("stock")>0:
            prodDic = {}
            prodDic["precio"]=v.get("precio")
            prodDic["stock"] = v.get("stock")
            productosFiltrados[k]=prodDic
    return productosFiltrados

productos = {
"Laptop": {"precio": 800.0 , "stock": 5},
"Raton": {"precio": 15.0, "stock": 10},
"Monitor": {"precio": 150.0 , "stock": 0},
"Teclado": {"precio": 55.0, "stock": 3}
}

resultado = filtrar_inventario(productos)
print(resultado)

