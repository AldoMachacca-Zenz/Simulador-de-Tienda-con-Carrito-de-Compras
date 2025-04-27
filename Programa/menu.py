from colorama import Fore
from Utilidades.errores import ErrorNoEsNumero, ErrorNumeroInvalido

# Mostrar el menu
def mostrar_menu():
    print(Fore.GREEN + "Que deseas hacer?")
    print(Fore.LIGHTBLUE_EX + "1. Ver catalogo\n")
    print("2. Agregar producto al carrito\n")
    print("3. Eliminar producto del carrito\n")
    print("4. Vaciar carrito\n")
    print("5. Mostrar carrito\n")
    print("6. Finalizar compra\n")
    print("7. Salir\n" + Fore.RESET)
    
def validar_opcion_menu_ingresado(option: str):
    if not option.isdigit():
        raise ErrorNoEsNumero("Debe ingresar un numero", codigo_error = 1)
    
    if int(option) not in range(1, 8):
        raise ErrorNumeroInvalido("Debe  ingresar un numero valido(1-7)", codigo_error = 2)
    
    return int(option)  

def opcion_menu():
    option = input("Elija un  opcion: ")
    option_new = validar_opcion_menu_ingresado(option)
    if option_new is not None:
        return option_new