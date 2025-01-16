import math

def area_cir(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Args:
        radio (float): El radio del círculo.
    
    Returns:
        float: El área del círculo.
    
    Ejemplo:
        >>> area_cir(5)
        78.53981633974483
    """
    return math.pi * radio ** 2

def vol_cilin(radio, altura):
    """
    Calcula el volumen de un cilindro dado su radio y altura,
    usando la función para calcular el área de la base (círculo).
    
    Args:
        radio (float): El radio de la base del cilindro.
        altura (float): La altura del cilindro.
    
    Returns:
        float: El volumen del cilindro.
    
    Ejemplo:
        >>> vol_cilin(5, 10)
        1570.7963267948967
    """
    area_base = area_cir(radio)  
    return area_base * altura

area = area_cir(5)
print("Área del círculo:", area)

# Calcular el volumen de un cilindro con radio 5 y altura 10
volumen = vol_cilin(5, 10)
print("Volumen del cilindro:", volumen)