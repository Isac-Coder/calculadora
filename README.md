<!--https://github.com/JavierArizaRiwi/MARKDOWN/blob/main/markdown_syntax_guide.md-->

<!--https://markdownlivepreview.com/-->

# **Proyecto: [Calculadora Científica](https://www.desmos.com/scientific?lang=es) Básica en Python**

Este scrit permite realizar operaciones matemáticas básicas y avanzadas mediante la selección de un menú interactivo.

## ***Código Fuente***

#####  1. Dentro de un ciclo le damos las opciones que el usuario puede realizar

```
    while True:   
        print("Bienvenido a la calculadora científica")
        print("Seleccione la operación que desea realizar:")
        print("1. Potencia")
        print("2. Raíz cuadrada del primer número")
        print("3. Porcentaje del primer número con respecto al segundo")
        print("4. Módulo (resto de la división)")
        print("5. Promedio de los dos números")
        print("6. Suma")
        print("7. Resta")
        print("8. Multiplicación")
        print("9. División")
        print("10. Desea continuar? (s/n)")
```

--------------------------------------------------------------------------

##### 2. agregamos el codigo de las operaciones que se pueden realizar en la calculadora

 ```
opcion = int(input("Ingrese el número de la operación que desea realizar: "))

    if opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 ** num2
        print(f"{num1} elevado a la {num2} es igual a {resultado}")

    elif opcion == 2:
        num1 = float(input("Ingrese el número: "))
        resultado = num1 ** 0.5
        print(f"La raíz cuadrada de {num1} es igual a {resultado}")

    elif opcion == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = (num1 / num2) * 100
        print(f"{num1} es el {resultado}% de {num2}")

    elif opcion == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 % num2
        print(f"El módulo de {num1} y {num2} es igual a {resultado}")

    elif opcion == 5:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = (num1 + num2) / 2
        print(f"El promedio de {num1} y {num2} es igual a {resultado}")

    elif opcion == 6:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es igual a {resultado}")

    elif opcion == 7:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es igual a {resultado}")

    elif opcion == 8:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es igual a {resultado}")

    elif opcion == 9:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
        resultado = num1 / num2
        print(f"La división de {num1} entre {num2} es igual a {resultado}")

    else:
         print("Error: No se puede dividir por cero.")

    elif opcion == 10:
        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
             print("Gracias por usar la calculadora científica. ¡Hasta luego!")
            break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")
```

------------------------

### Este seria el codigo de la calculadora aun esta en proceso asi que tranquilos

###### Más actualizaciones pronto 😄