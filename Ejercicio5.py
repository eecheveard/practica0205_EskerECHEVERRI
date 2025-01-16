def cuadrados(lista_numeros):
    """
    Calcula el cuadrado de cada número en una lista.
    
    Parámetros:
        lista_numeros (list): Una lista de números (int o float).
    
    Devuelve:
        list: Una lista con los valores al cuadrado de los números originales.
    """
    return [num ** 2 for num in lista_numeros]

# Ejemplo de uso
muestra = [2, 4, 6, 8]
resultado = cuadrados(muestra)
print(f"Los valores al cuadrado son: {resultado}")