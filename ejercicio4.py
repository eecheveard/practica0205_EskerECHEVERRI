def calcular_media(lista_numeros):
    """
    Calcula la media de una lista de números.
    
    Parámetros:
        lista_numeros (list): Una lista de números (int o float).
    
    Devuelve:
        float: La media de los números en la lista.
    """
    if not lista_numeros:
        raise ValueError("La lista no puede estar vacía.")
    
    suma = sum(lista_numeros)
    cantidad = len(lista_numeros)
    return suma / cantidad

# Ejemplo:
muestra = [3, 5, 7, 9]
media = calcular_media(muestra)
print(f"La media de la muestra es: {media}")