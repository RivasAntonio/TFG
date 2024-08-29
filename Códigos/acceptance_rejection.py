import numpy as np
import matplotlib.pyplot as plt

lam = 0.5

def exponential_pdf(x):
    """Función de distribución de probabilidad exponencial"""
    return lam * np.exp(-lam * x)

def acceptance_rejection_sampling(pdf, N): #M=número máximo de la distribución exponencial, N=número de samples que quiero
    """Algoritmo sampleo acceptance-rejection method"""
    samples = []#Creo la lista de los números aleatorios vacía
    while len(samples) < N:
        x = np.random.rand() * (4./lam) # Sampleamos uniformemente los números
        y = np.random.rand() * lam # Escalamos el sampleo al valor máximo de la función de distribución de probabilidad
        if y <= pdf(x):
            samples.append(x) #Añadimos x a a lista de los números
    return samples


# Sampleamos los 1000 números usando el método 
samples = acceptance_rejection_sampling(exponential_pdf, 10000)

# Ploteamos el histograma
plt.hist(samples, bins=50, density=True)
plt.xlabel('x')
plt.ylabel('Frecuencia')
plt.title('Distribución exponencial')
plt.show()
