def regla30(a, b, c):
    """
    Implementa la Regla 30:
    f(a, b, c) = a XOR (b OR c)
    donde a, b, c son los estados (0 o 1) de la celda izquierda,
    central y derecha, respectivamente.
    """
    return a ^ (b or c)

def siguiente_fila(config):
    """
    Dada una configuración (lista de 0s y 1s),
    calcula la siguiente fila usando la Regla 30.
    Se asumen bordes fijos en 0.
    """
    n = len(config)
    nueva = [0] * n
    for i in range(n):
        left   = config[i-1] if i > 0     else 0
        center = config[i]
        right  = config[i+1] if i < n-1   else 0
        nueva[i] = regla30(left, center, right)
    return nueva

def imprimir_config(config):
    """
    Imprime una configuración reemplazando:
    1 -> '█'  y  0 -> ' ' (espacio).
    Esto permite ver el patrón de forma más clara.
    """
    linea = ''.join('█' if c == 1 else ' ' for c in config)
    print(linea)

# Parámetros de la simulación
num_celdas = 61   # longitud de la fila
pasos = 30        # número de iteraciones en el tiempo

# Condición inicial: una sola celda en 1 en el centro
config = [0] * num_celdas
config[num_celdas // 2] = 1

# Evolución temporal
for t in range(pasos + 1):
    imprimir_config(config)
    config = siguiente_fila(config)
