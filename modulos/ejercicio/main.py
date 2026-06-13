import tienda as tnd 
import menu
carrito = []
opcion = menu.ejecutar_menu()
while opcion!=0:
    if opcion == 1:
        tnd.mostrar_productos()
    if opcion == 2:
        nombrePro = input(menu.menuProducto)
        cantPro = int(input(menu.menuCantidad))
        tnd.agregar_carrito(carrito,(nombrePro,cantPro))
    if opcion == 3:
        tnd.mostrar_estado_carrito(carrito)
    if opcion == 4:
        tnd.calcular_total(carrito)
    opcion = menu.ejecutar_menu()
    


        
