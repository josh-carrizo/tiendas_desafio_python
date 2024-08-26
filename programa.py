from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

supermercado = Supermercado("Supermercado Latam", 5000)
farmacia = Farmacia("Farmacia Python", 3500)
restaurante = Restaurante("Restaurante donde el Josh", 12000)

terminar_operacion = False

def SelecionTienda():
    opcion_tienda = int(input("Seleccione la tienda en la que desea interactuar:\n1. Supermercado\n2. Farmacia\n3. Restaurante\n> "))
    if opcion_tienda == 1:
        return supermercado
    elif opcion_tienda == 2:
        return farmacia
    elif opcion_tienda == 3:
        return restaurante
    else:
        print("Tienda no encontrada en las opciones")

while terminar_operacion == False:
    opcion = int(input("Seleccione una acción:\n1. Ingresar producto\n2. Listar productos\n3. Realizar venta\n0. Salir\n> "))
    if opcion == 0:
        print("Has salido del programa, vuelve pronto! :)")
        terminar_operacion == True
        exit()
    
    elif opcion == 1:
        tienda = SelecionTienda()
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        stock = int(input("Stock del producto: "))
        producto = Producto(nombre, precio, stock)
        tienda.NuevoProducto(producto)
        
    elif opcion == 2:
        tienda = SelecionTienda()
        print(tienda.ListaProductos())
        
    elif opcion == 3:
        tienda = SelecionTienda()
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        if tienda.RealizarVenta(nombre, cantidad):
            print("Venta realizada con éxito.")
            
        else:
            print("Venta fallida.")
    else:
        print("Opción no válida")
        exit()        