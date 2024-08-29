import random
import math
import numpy as np
import matplotlib.pyplot as plt

def inverse_transform(n, lam):
    """Generate n random numbers from an exponential distribution with rate parameter lam using inverse transform method"""
    # genera variable aleatoria U(0,1)
    u = np.random.rand(n) #Crea un vector de números aleatorios
    # Transforma la función U(0,1) a una distribución exponencial usando el método de la transformada inversa
    x = -np.log(u) / lam 
    return x

# Ajusto el parámetro al del ejercicio, 2
lam = 2

# Sampleamos los 1000 valores
#x = inverse_transform(10000, lam)
y = np.random.randn(1000000)
# pintamos el histograma
yhist, xhist, _ = plt.hist(y, bins=100, density=True) 
#Guardo los datos que voy a pintar, primero la función 'altura', luego el argumento de esta, la 'anchura'
p = 1/np.sqrt(2*np.pi)*np.exp(-(xhist)**2/2)
plt.plot(xhist, p, '-')
plt.xlabel('x',fontsize=18)
plt.ylabel('Frecuencia',fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend()
plt.title('Distribución gaussiana',fontsize=18)
plt.show()

