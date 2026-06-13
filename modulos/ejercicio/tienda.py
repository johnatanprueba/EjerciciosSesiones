INVENTARIO = {
    "Laptop": 800.0,
    "Teclado": 45.0,
    "Raton": 25.0,
    "Monitor": 150.0
}

def calcular_total(carrito):
    costoTotal = 0
    for tpl in carrito:
        producto = tpl[0]
        cantidad = tpl[1]
        precio = INVENTARIO[producto]
        costo = cantidad*precio
        costoTotal = costoTotal+costo
    if costoTotal > 500:
        costoTotal = costoTotal*0.9
    print(f"Costo total:{costoTotal}")

def mostrar_productos():
    for k,v in INVENTARIO.items():
        print(f"{k} precio {v}") 

def agregar_carrito(carrito,tpl):
    producto = tpl[0]
    try:
        precio = INVENTARIO[producto]
        carrito.append(tpl)
    except KeyError as e:
        print("El producto no existe en el inventario ")

def mostrar_estado_carrito(carrito):
    for ele in carrito:
        print(f"{ele[0]} tiene {ele[1]} unidades")
    
    



    