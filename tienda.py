#3 tipo de tienda "Restaurante" "Supermercado " y "Farmacia"
#Acciones: Ingresar Producto, listar productos existentes y realizar ventas
#Cada tienda tiene un nombre, listado de productos (Inicialmente 0), y costo delivery 
        #No se puede modificar nombre ni costo, pero si los productos:>> ingreso_producto o realizar_venta

from producto import Producto

class Tienda():
    def __init__(self, producto: str, envio:int):
        self.__producto = producto
        self.__envio = envio
        self.__productos = []
        
    @property
    def producto(self):
        return self.__producto
    @property
    def envio(self):
        return self.__envio    

    def NuevoProducto(self, producto: Producto):
        for p in self.__productos:
            if p.nombre == producto.nombre:
                p.stock += producto.stock
                return
        self.__productos.append(producto)
    
    def ListaProductos(self):
        retorno = ("::::::::Lista de Productos::::::::\n"
                    "Nombre producto \tCantidad \t Precio\n")
        ver_productos=[f'{i.nombre}\t\t{i.stock}\t\t{i.precio}\n' for i in self.__productos ]
        return f'{retorno}{''.join(ver_productos)}'
        
    def RealizarVenta(self, nombre_producto, cantidad):
        for p in self.__productos:
            if p.nombre == nombre_producto:
                if isinstance(self, Restaurante):
                    return True  
                elif p.stock >= cantidad:
                    p.stock = p.stock - cantidad
                    return True
                else:
                    return False
        return False    

class Supermercado(Tienda):
    def ListaProductos(self):
        result = []
        for p in self._Tienda__productos:
            retorno = ("::::::::Lista de Productos::::::::\n"
                    "Nombre producto \tPrecio \t\t Cantidad\n")
            stock_msg = f"Pocos productos disponibles ({p.stock})" if p.stock < 10 else f"Stock: {p.stock}"
            result.append(f"{retorno}{p.nombre.title()} \t\t\t{p.precio} \t\t {stock_msg}")
        return f'{retorno}\n'.join(result)
    

class Farmacia(Tienda):
    def ListaProductos(self):
        result = []
        retorno = ("\n::::::::Lista de Productos::::::::\n"
        "Nombre producto \tPrecio \t\t Promoción\n") 
        for p in self._Tienda__productos:           
            envio_msg = "Envío gratis al solicitar este producto" if p.precio > 15000 else "El producto no posee promoción"
            result.append(f"{retorno}{p.nombre.title()} \t\t\t{p.precio} \t\t {envio_msg}")
        return f'{retorno}\n'.join(result)

    def RealizarVenta(self, nombre_producto, cantidad):
        if cantidad > 3:
            return False
        return super().RealizarVenta(nombre_producto, cantidad)
        
    
class Restaurante(Tienda):
    def RealizarVenta(self, nombre_producto, cantidad):
        return True

