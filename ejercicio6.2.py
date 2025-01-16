def binario_a_decimal(binario):
    """
    Convierte un número binario a su representación decimal.
    
    Parámetros:
        binario (str): El número binario a convertir.
    
    Devuelve:
        int: La representación decimal del número.
    """
    try:
        return int(binario, 2)
    except ValueError:
        raise ValueError("La cadena debe ser un número binario válido.")

# Ejemplo
numero_binario = "1010"
decimal = binario_a_decimal(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {decimal}")