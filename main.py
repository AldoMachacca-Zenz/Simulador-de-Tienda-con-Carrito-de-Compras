from colorama import Fore, Style
from Utilidades.errores import ErrorNoEsNumero, ErrorNumeroInvalido, ErrorCarritoVacio, ErrorProductoNoEncontrado
from Utilidades.helpers import limpiar_pantalla
from Programa.gestor import acciones_del_menu
from Programa.menu import mostrar_menu, opcion_menu
from Modelos.productos import catalogo_productos
from Modelos.carrito import carrito

while True:
    try: 
        print(Fore.WHITE + Style.BRIGHT + "Bienvenido a la tienda virtual\n")
        mostrar_menu()
        option = opcion_menu()
        acciones_del_menu(option, catalogo_productos, carrito)
        
    except ErrorNoEsNumero as e:
        limpiar_pantalla()
        print(Fore.RED + f"⚠️  Error {e.codigo_error} tipo de dato:{e}")
    except ErrorNumeroInvalido as e:
        limpiar_pantalla()
        print(Fore.RED + f"⚠️  Error {e.codigo_error} numero invalido: {e}")
    except ErrorCarritoVacio as e:
        limpiar_pantalla()
        print(Fore.RED + f"⚠️  Error {e.codigo_error} carrito vacio: {e}")
    except ErrorProductoNoEncontrado as e:
        limpiar_pantalla()
        print(Fore.RED + f"⚠️  Error {e.codigo_error} producto no encontrado: {e}")