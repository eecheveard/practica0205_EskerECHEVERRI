def factorial_iter(num):
    """
    Calcula el factorial de un número.
    
    Args:
        num (int): Número entero positivo para el cual se calculará el factorial.
    
    Returns:
        int: El factorial de num.
    
    Ejemplo:
        >>> factorial_iter(5)
        120
    """
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado
    
resultado = factorial_iter(5)
print(resultado)