from collections import deque
from colorama import Style,Fore
from Servicios.catalogo import buscar_producto_lista
from Utilidades.errores import ErrorNoEsNumero, ErrorProductoNoEncontrado, ErrorCarritoVacio 
from Datos.historial import guardar_historia_compra
from Utilidades.helpers import simulacion_de_carga

def recorrer_iterable(iterable: deque):
    if len(iterable) > 0:
        for i in  iterable:
            print(Fore.WHITE + f"✔️  {i["nombre"]} (" + Fore.YELLOW + f"x{i["cantidad"]}" + Fore.RESET + f")  ⏩  S/ {i["precio"]}")
    else:
        raise ErrorCarritoVacio("Debe agregar productos al carrito", codigo_error = 4)

def agregar_productos_al_carrito(catalogo_productos, carrito: deque):
    print(Fore.GREEN + "AGREGAR PRODUCTO AL CARRITO 🛒 \n")
    codigo_producto = input(Fore.RESET + "Ingrese codigo producto: ")
    # Buscamos si existe el producto
    existe, posicion = buscar_producto_lista(catalogo_productos,"codigo", codigo_producto)
    
    if existe:
        cantidad = input("Cantidad: ")
        
        if not cantidad.isdigit(): raise ErrorNoEsNumero("Debe ingresar un numero", codigo_error = 1)
        
        carrito.append({"nombre": catalogo_productos[posicion]["nombre"], "cantidad": cantidad, "precio": (catalogo_productos[posicion]["precio"]) * int(cantidad)})
        simulacion_de_carga("agregando producto", 0.3, f"El producto " + Fore.CYAN + f"{catalogo_productos[posicion]["nombre"]} " + Fore.RESET + "fue agregado satisfactoriamente")
        input("...")
        
    else:
        raise ErrorProductoNoEncontrado("Producto no encontrado en catalogo de productos", codigo_error = "5")
        
def mostrar_carrito(carrito: deque):
    print(Fore.GREEN + "TU CARRITO")
    recorrer_iterable(carrito)
    
def eliminar_producto_carrito(carrito: deque):
    # Mostramos elemento de carrito
    mostrar_carrito(carrito)
    print("\n")
    print(Fore.GREEN + "ELIMINAR PRODUCTO DEL CARRITO")
    print("\n")
    producto = input(Fore.RESET  + "Ingresa el nombre del producto: ")
    # Buscamos si es que existe el carrito
    existe, posicion = buscar_producto_lista(carrito, "nombre", producto.lower())
    if existe:
        del carrito[posicion]
        print("Se elimino correctamente " + Fore.CYAN + f"{producto}" + Fore.RESET + " del carrito")
        input("...")
    else:
        raise ErrorProductoNoEncontrado("Producto no encontrado en el carrito", codigo_error = "5")

def vaciar_carrito(carrito: deque):
    while len(carrito) > 0:
        carrito.pop()
    print("Se vacio correctamente el carrito")
    
def finalizar(carrito: deque):
    suma_total = 0
    print(Fore.GREEN + "📝RESUMEN DE COMPRA: ")
    recorrer_iterable(carrito)
    for producto in carrito:
        suma_total += producto["precio"]
    print(Fore.LIGHTBLACK_EX + f"Total a pagar: S/ {suma_total}")
    print(Style.BRIGHT + Fore.BLUE + "Gracias por su compra!!! 🤝")
    guardar_historia_compra(carrito, suma_total)
    input("...")
    exit()