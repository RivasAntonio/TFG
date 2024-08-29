import numpy as np
import matplotlib.pyplot as plt
# Definimos la función transformada inversa
def inverse_transform(x):
    return -0.5 * np.log(1 - x)

# Generamos los 1000 números aleatorios entre 0 y 1 uniformemente distribuidos
u = np.random.uniform(0, 1, size=1000)#valor min, valor máx, size == número de valores que queremos 

# Aplicamos la transformada inversa para obtener los números aleatorios distribuidos exponencialmente
x = inverse_transform(u)

# Imprime los 1000 números
#print(x[:1000])
#Podemos poner el histograma
plt.hist(x, bins=50, density=True)
plt.xlabel('x')
plt.ylabel('Frecuencia')
plt.title('Distribución exponencial')
plt.show()