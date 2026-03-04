import time
from colores import *

def cargar():
    print(f"{VERDE}Calculando", end="")
    for _ in range(4):
        time.sleep(1)
        print(".", end="", flush=True)