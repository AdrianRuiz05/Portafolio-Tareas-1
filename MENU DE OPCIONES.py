def binario_a_decimal(binario):
    decimal = int(binario, 2)
    return decimal

def decimal_a_binario(decimal):
    binario = bin(decimal).replace("0b", "")
    return binario
while True:
    print("Selecciona una opción:")
    print("1. Convertir de binario a decimal")
    print("2. Convertir de decimal a binario")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar")
    print("6. Restar")
    print("7. Salir")
    opcion = input("Ingresa el número de la opcion que deseas obtener: ")

    if opcion == "1":
        binario = input("Ingresa un número binario: ")
        decimal = binario_a_decimal(binario)
        print(f"El equivalente decimal obtenido es: {decimal}")
    elif opcion == "2":
        decimal = int(input("Ingresa un número decimal: "))
        binario = decimal_a_binario(decimal)
        print(f"El equivalente binario obtenido es: {binario}")
    elif opcion == "3":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == "4":
        num1 = float(input("Ingresa el dividendo: "))
        num2 = float(input("Ingresa el divisor: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("No se puede dividir por cero.")
    elif opcion == "5":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "6":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "7":
        print(" Gracias por utilizar mi codigo ¡Hasta luego! :DD")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida (1-7).")
        