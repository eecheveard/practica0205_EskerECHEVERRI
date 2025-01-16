def factorial_recu(num):
    """
    Calcula el factorial de un número de manera recursiva.
    
    Args:
        num (int): Número entero positivo para el cual se calculará el factorial.
    
    Returns:
        int: El factorial de num.
    """
    if num == 0 or n == 1:
        return 1
    else:
        return num * factorial_recu(num - 1)