# **Proyecto: Calculadora Científica Básica en Python**

Este script permite realizar operaciones matemáticas básicas y avanzadas mediante la selección de un menú interactivo.

## ***Código Fuente***

 Pedimos al usuario el primer número y lo convertimos a entero

    x = int(input("ingrese un digito"))


Pedimos al usuario el segundo número y lo convertimos a entero

    y = int(input("ingrese otro digito"))


Mostramos un menú con las opciones de cálculo y capturamos la opción elegida

    opcion = input("Ingrese la opción de calculo deseado: "
          "Opciones de cálculo disponibles:\n"
          "1: Suma\n"
          "2: Resta\n"
          "3: Multiplicación\n"
          "4: División\n"
          "5: Potencia\n"
          "6: Raíz cuadrada\n"
          "7: Porcentaje\n"
          "8: Módulo (%)\n"
          "9: Promedio de dos números\n")


Verificamos qué opción eligió el usuario y realizamos la operación correspondiente

     Suma
      if opcion == "1": 
        resultado = x + y
        print("El resultado de la suma es:", resultado)
        
    Resta
      elif opcion == "2":
          resultado = x - y
          print("El resultado de la resta es:", resultado)
    
    Multiplicacion
      elif opcion == "3":
          resultado = x * y
          print("El resultado de la multiplicación es:", resultado)         
    
    Division
      elif opcion == "4":
          if y != 0:
              resultado = x / y
              print("El resultado de la división es:", resultado)
      else:
          print("Error: No se puede dividir por cero.")
        
    Potencia
      elif opcion == "5":
          resultado = x ** y
          print("El resultado de la potencia es:", resultado)
      elif opcion == "6":
          if x >= 0:
              resultado = x ** 0.5
              print("El resultado de la raíz cuadrada es:", resultado)
          else:
              print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
      elif opcion == "7":
          resultado = (x / y) * 100
          print("El resultado del porcentaje es:", resultado, "%")
      elif opcion == "8":
              if y != 0:
                  resultado = x % y
                  print("El resultado del módulo es:", resultado)
              else:
                  print("Error: No se puede calcular el módulo con divisor cero.")
      elif opcion == "9":
          resultado = (x + y) / 2
          print("El resultado del promedio es:", resultado)
      else:    print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")    

  Aqui el codigo completo

  
