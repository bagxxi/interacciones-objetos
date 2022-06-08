from tienda import Tienda, TiendaRestaurante, TiendaSupermercado, TiendaFarmacia
from producto import Producto

tipo = int(input("Ingrese tipo de comercio a agregar:\n"
                 "1. Restaurante\n2. Supermercado\n3. Farmacia\n"))
nombre = input("\nIngrese nombre de la tienda a agregar:\n")
precio_delivery = int(input("\nIngrese precio del deliveyr:\n"))

if tipo == 2:
    tienda = TiendaSupermercado(nombre, precio_delivery)
elif tipo == 3:
    tienda = TiendaFarmacia(nombre, precio_delivery)
else:
    tienda = TiendaRestaurante(nombre, precio_delivery)

opcion = 1

while opcion == 1:
    nombre_producto = input("\nIngrese nombre del producto a ingresar:\n")
    precio = int(input("\nIngrese precio del producto:\n"))
    stock = int(input("\nIngrese stock del producto:\n"))
    tienda.ingresar_producto(nombre_producto, precio, stock)

    opcion = int(input("\n¿Desea agregar otro producto?\n"
                       "1. Sí\n2. No\n"))

opcion_productos = int(input("\nIndique qué desea realizar:\n"
                             "1. Listar productos de la tienda\n"
                             "2. Realizar una venta de producto\n"
                             "3. Salir\n"))

while opcion_productos in [1, 2]:
    if opcion_productos == 1:
        print(tienda.listar_productos())
    elif opcion_productos == 2:
        nombre_producto = input("\nIngrese nombre del producto a vender:\n")
        cantidad = int(input("\nIngrese cantidad que desea comprar:\n"))
        tienda.realizar_venta(nombre_producto, cantidad)

    opcion_productos = int(input("\nIndique qué desea realizar:\n"
                                 "1. Listar productos de la tienda\n"
                                 "2. Realizar una venta de producto\n"
                                 "3. Salir\n"))