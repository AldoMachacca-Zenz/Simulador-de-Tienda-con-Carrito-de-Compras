from collections import deque
from colorama import Fore

def mostrar_catalogo(catagolo_productos: deque):
    print("CATALOGO DE PRODUCTOS")
    for producto in catagolo_productos:
        print(Fore.WHITE + "codigo: " + Fore.LIGHTBLACK_EX + f"{producto["codigo"]} " + Fore.GREEN + "|" + Fore.WHITE + " nombre:" + Fore.LIGHTBLACK_EX + f"{producto["nombre"]} " + Fore.GREEN +"|" + Fore.WHITE + " precio: " + Fore.LIGHTBLACK_EX + f"S/{producto["precio"]}")
        
def buscar_producto_lista(lista, tipo: str, objetivo: str):
    lista_ordenada = sorted(lista, key=lambda x: x[tipo])  # Ordenar según el tipo
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        producto_medio = lista_ordenada[medio]  # Obtener el producto en la posición 'medio'
        
        # Comparar el valor del tipo especificado
        if producto_medio[tipo] == objetivo:
            # Obtener la posición original en la lista
            posicion_original = lista.index(producto_medio)
            return True, posicion_original  # Retorna True y la posición en la lista original
        elif producto_medio[tipo] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False, -1  # No encontrado