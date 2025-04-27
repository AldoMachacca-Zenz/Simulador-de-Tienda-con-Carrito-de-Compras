from Utilidades.helpers import simulacion_de_carga, limpiar_pantalla
from Servicios.gestion_carrito import * # importamos todas las funciones
from Servicios.catalogo import mostrar_catalogo

def acciones_del_menu(numero: int, catalogo_productos: deque, carrito: deque):
    if numero == 1:
        simulacion_de_carga("Cargando...", 0.3, "Carga completada")
        # Funcion mostrar catalogo
        mostrar_catalogo(catalogo_productos)
        input("...") # stop al programa
        limpiar_pantalla()
        
    elif numero == 2:
        mostrar_catalogo(catalogo_productos)
        print("\n")
        # Funcion agregar carrito
        agregar_productos_al_carrito(catalogo_productos, carrito)
        limpiar_pantalla()
        
    elif numero == 3:
        # Eliminar producto del carrito
        eliminar_producto_carrito(carrito)
        limpiar_pantalla()
        
    elif numero == 4:
        simulacion_de_carga("Vaciando...", 0.3, "procesamiento completado")
        # Funcion vasear carrito
        vaciar_carrito(carrito)
        limpiar_pantalla()
        
    elif numero == 5:
        simulacion_de_carga("Cargando...", 0.3, "carga completa")
        # Mostrar carrito
        mostrar_carrito(carrito)
        input("...")
        limpiar_pantalla()
        
    elif numero == 6:
        simulacion_de_carga("Finalizando compra...", 0.3, "boleta generada")
        print("\n")
        # Funcion finalizar compra
        finalizar(carrito)
        
    elif numero == 7:
        exit()