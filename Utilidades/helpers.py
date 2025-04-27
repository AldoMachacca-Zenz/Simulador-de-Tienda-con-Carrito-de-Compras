import os, sys
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def simulacion_de_carga(mensaje: str, rapidez: float, mensaje_final: str):
    for _ in range(5):  # Número de veces que parpadeará
        sys.stdout.write("\r" + mensaje)  # Escribe el mensaje en la misma línea
        sys.stdout.flush()  # Refresca la salida para que se actualice
        time.sleep(rapidez)  # Espera medio segundo

        sys.stdout.write("\r" + " " * len(mensaje))  # Borra el mensaje sin limpiar pantalla
        sys.stdout.flush()
        time.sleep(rapidez)  # Espera antes de volver a imprimir
    print(f"\r✅ {mensaje_final}")