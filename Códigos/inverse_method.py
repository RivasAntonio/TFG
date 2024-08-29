import random
import math
import numpy as np
import matplotlib.pyplot as plt

def inverse_transform(n, lam):
    """Generate n random numbers from an exponential distribution with rate parameter lam using inverse transform method"""
    # genera variable aleatoria U(0,1)
    u = [random.random() for i in range(n)]
    # Transforma la función U(0,1) a una distribución exponencial usando el método de la transformada inversa
    x = [-math.log(i) / lam for i in u]
    return x

# Ajusto el parámetro al del ejercicio, 2
lam = 2

# Sampleamos los 1000 valores
x = inverse_transform(100, lam)

# pintamos el histograma
yhist, xhist, _ = plt.hist(x, bins=10, density=True) #(datos a pintar, bins=define cuantas columnas tiene el histograma, density=true--->Pinta densidad de probabilidad
p = lam*np.exp(-lam*xhist)
plt.plot(xhist, p, '-')
plt.xlabel('x')
plt.ylabel('Frecuencia')
plt.title('Distribución exponencial')
plt.show()

