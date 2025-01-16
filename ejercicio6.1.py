def decimal_a_binario(decimal):
    """
    Convierte un número decimal a su representación binaria.
    
    Parámetros:
        decimal (int): El número decimal a convertir.
    
    Devuelve:
        str: La representación binaria del número.
    """
    if decimal < 0:
        raise ValueError("El número debe ser un entero positivo.")
    return bin(decimal)[2:]

# Ejemplo
numero_decimal = 10
binario = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {binario}")