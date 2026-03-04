from colores import *
from carga import cargar
from LimpiarP import LP
historial = []


while True:
    print(f"{VERDE}Bienvenido a la calculadora científica")
    print(f"Estas son las operaciones disponibles:")
    print(f"1. Potencia del primer número elevado al segundo número")
    print(f"2. Raíz cuadrada")
    print(f"3. Porcentaje del segundo número con respecto al primer número")
    print(f"4. Módulo (resto de la división) del primer número entre el segundo número")
    print(f"5. Promedio de los dos números")
    print(f"6. Suma")
    print(f"7. Resta")
    print(f"8. Multiplicación")
    print(f"9. División")
    print(f"{VERDE}10. Ver historial de operaciones")
    print(f"{ROJO}11. Salir{VERDE}\n")

    opcion = int(input("Ingrese el número de la operación que desea realizar: "))
    
    if opcion == 1:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 ** num2
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}{num1} elevado a la {num2} es igual a {resultado}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}{num1} elevado a la {num2} es igual a {resultado}\n")
        historial.append(f"{num1} elevado a la {num2} = {resultado}")
        
    elif opcion == 2:
        LP()
        num1 = float(input("Ingrese el número: "))
        resultado = num1 ** 0.5
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}La raíz cuadrada de {num1} es igual a {resultado}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}La raíz cuadrada de {num1} es igual a {resultado}\n")
        historial.append(f"Raíz cuadrada de {num1} = {resultado}")
        
    elif opcion == 3:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = (num1 / num2) * 100
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}{num1} es el {resultado}% de {num2}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}{num1} es el {resultado}% de {num2}\n")
        historial.append(f"{num1} es el {resultado}% de {num2}")
        
    elif opcion == 4:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 % num2
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}El módulo de {num1} y {num2} es igual a {resultado}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}El módulo de {num1} y {num2} es igual a {resultado}\n")
        historial.append(f"Módulo de {num1} y {num2} = {resultado}")
        
    elif opcion == 5:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = (num1 + num2) / 2
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}El promedio de {num1} y {num2} es igual a {resultado}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}El promedio de {num1} y {num2} es igual a {resultado}\n")
        historial.append(f"Promedio de {num1} y {num2} = {resultado}")
        
    elif opcion == 6:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}La suma de {num1} y {num2} es igual a {resultado}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}La suma de {num1} y {num2} es igual a {resultado}\n")
        historial.append(f"Suma de {num1} y {num2} = {resultado}")
        
    elif opcion == 7:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}La resta de {num1} y {num2} es igual a {resultado}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}La resta de {num1} y {num2} es igual a {resultado}\n")
        historial.append(f"Resta de {num1} y {num2} = {resultado}")
        
    elif opcion == 8:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        cargar()
        print("\n")
        if resultado.is_integer():
            resultado = int(resultado)
            print(f"{VERDE}La multiplicación de {num1} y {num2} es igual a {resultado}\n")
        else:
            resultado = round(resultado, 2)
            print(f"{VERDE}La multiplicación de {num1} y {num2} es igual a {resultado}\n")
        historial.append(f"Multiplicación de {num1} y {num2} = {resultado}")
        
    elif opcion == 9:
        LP()
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            cargar()
            print("\n")
            if resultado.is_integer():
                resultado = int(resultado)
                print(f"{VERDE}La división de {num1} entre {num2} es igual a {resultado}\n")
            else:
                resultado = round(resultado, 2)
                print(f"{VERDE}La división de {num1} entre {num2} es igual a {resultado}\n")
            historial.append(f"División de {num1} entre {num2} = {resultado}")
        else:
            print(f"{ROJO}Error: No se puede dividir por cero.{ROJO}\n")
            
    elif opcion == 11:
        continuar = input(f"{ROJO}¿Desea realizar otra operación? (s/n): {VERDE}")
        if continuar.lower() != 's':
            print(f"{VERDE}Gracias por usar la calculadora científica. ¡Hasta luego!")
            break
    elif opcion == 10:
        if not historial:
            print(f"{ROJO}No hay operaciones en el historial.{RESET}\n")
        else:
            cargar()
            print("\n")
            LP()
            print(f"{AMARILLO}┌───────────┐")
            print("│ HISTORIAL │")
            print("└───────────┘\n")
            print(f" =======================================")
            for i, operacion in enumerate(historial, 1):
                print(f"| {i}. {operacion}")
            print(" =======================================\n")
        continue
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 11.\n")