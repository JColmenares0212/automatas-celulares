"""
Regla 110 - Ejemplo 2
Condición inicial: configuración aleatoria de celdas.
Visualización con caracteres tipo bloque.

Autor: Julian Dario Colmenares Saenz
"""

import random


#   Definición de la Regla 110
def regla110(a, b, c):
    """
    Implementa la Regla 110 según su tabla de transición.
    Los patrones se codifican como un número entre 0 y 7.
    """
    # Tabla en el orden 000,001,010,011,100,101,110,111
    mapping = [0, 1, 1, 1, 0, 1, 1, 0]

    idx = (a << 2) | (b << 1) | c  # convertir el trío a número decimal
    return mapping[idx]


#   Cálculo de la siguiente fila
def siguiente_fila(config):
    """
    Dada una configuración actual (lista de 0s y 1s),
    calcula la fila siguiente aplicando la Regla 110.
    Bordes fijos en 0.
    """
    n = len(config)
    nueva = [0] * n

    for i in range(n):
        left   = config[i-1] if i > 0     else 0
        center = config[i]
        right  = config[i+1] if i < n-1   else 0
        nueva[i] = regla110(left, center, right)

    return nueva


#   Visualización de la configuración
def imprimir_config(config):
    """
    Imprime la configuración usando:
    1 -> '█'
    0 -> ' '
    """
    linea = ''.join('█' if c == 1 else ' ' for c in config)
    print(linea)


#   Simulación principal
if __name__ == "__main__":
    num_celdas = 100
    pasos = 80   # mismo número de iteraciones que en el ejemplo 1

    # Condición inicial: configuración aleatoria
    config = [random.randint(0, 1) for _ in range(num_celdas)]

    print("Regla 110 - Ejemplo 2: Condición inicial aleatoria (100 celdas, 80 iteraciones)\n")

    for t in range(pasos + 1):
        imprimir_config(config)
        config = siguiente_fila(config)
