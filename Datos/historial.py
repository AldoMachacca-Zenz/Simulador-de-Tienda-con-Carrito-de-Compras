from datetime import datetime
from collections import deque
import csv
import os
from colorama import Fore

def guardar_historia_compra(mi_carrito: deque, suma_total_compra: float):
    fecha_hora_actual = [str(datetime.now())]
    nombre_archivo = "historial.csv"
    
    if not os.path.exists(nombre_archivo):
        print(Fore.YELLOW + "Archivo de historial creado")
        with open(nombre_archivo, mode = "w", newline = "", encoding = "utf-8") as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow(fecha_hora_actual)
            escritor_csv.writerow(["Nombre", "Cantidad", "Precio"])
            for producto in  mi_carrito:
                escritor_csv.writerow([producto["nombre"], producto["cantidad"], producto["precio"]])
            escritor_csv.writerow([f"Suma total de compra: {suma_total_compra}"])
    else:
        with open(nombre_archivo, mode="a", newline="", encoding="utf-8") as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow([])
            escritor_csv.writerow(fecha_hora_actual)
            escritor_csv.writerow(["Nombre", "Cantidad", "Precio"])
            for producto in  mi_carrito:
                escritor_csv.writerow([producto["nombre"], producto["cantidad"], producto["precio"]])
            escritor_csv.writerow([f"Suma total de compra: S/ {suma_total_compra}"])
        print(Fore.YELLOW + "Se a aniadido al historial")