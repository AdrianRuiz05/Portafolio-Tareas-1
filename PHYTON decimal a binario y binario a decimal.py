def decimal_a_binario(decimal_numero):
    binario_numero = bin(decimal_numero)
    return binario_numero
    
def binario_a_decimal(binario_numero):
    decimal_numero = int(binario_numero, 2)
    return decimal_numero
        
# Solicitar al usuario que ingrese un número decimal
decimal = int(input("Ingresa un número decimal: "))

# Solicitar al usuario que ingrese un número binario
binario = input("Ingresa un número binario: ")

# Conversión de decimal a binario
resultado_binario = decimal_a_binario(decimal)
print(f'{decimal} en binario es: {resultado_binario}')

# Conversión de binario a decimal
resultado_decimal = binario_a_decimal(binario)
print(f'{binario} en decimal es: {resultado_decimal}')