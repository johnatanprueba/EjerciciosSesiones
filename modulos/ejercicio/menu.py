menu = "Digite la opcion que desea"
menu +="\n1.ver productos disponibles" 
menu +="\n2.Añadir producto y su cantidad"
menu +="\n3.ver el estado del carrito de compras"
menu +="\n4.Calcular total compra"
menu +="\n0.Pagar y/o Salir\n"

menuProducto = "Digite el nombre del producto\n"
menuCantidad = "Digite la cantidad del producto\n"

def ejecutar_menu():
    opcion = int(input(menu))
    return opcion