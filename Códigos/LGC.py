import numpy as np #lo llamamos np para escribir menos
import time #Para saber cuánto tarda cada proceso
import sys
import random
import matplotlib.pyplot as plt

def LGC(N,s): #cantidad de números que quiero, semilla
    a=9
    M=1103
    b=1
    def f(s):
        return (a*s+b) % M
    U=[]
    for i in range(N):
        s=f(s)
        U += [s/M]
    return U

#Malas opciones serán con M pequeño, probar con diferentes semillas

#print(LGC(10,2))# a=3**7,M=2**8 b=7**3 [0.7, 0.2, 0.7, 0.2, 0.7, 0.2, 0.7, 0.2, 0.7, 0.2]
#print(LGC(30,1))# a=3**7,M=2**8 b=7**3  [0.0, 0.3, 0.4, 0.1, 0.0, 0.3, 0.4, 0.1, 0.0, 0.3, 0.4, 0.1, 0.0, 0.3, 0.4, 0.1, 0.0, 0.3, 0.4, 0.1, 0.0, 0.3, 0.4, 0.1, 0.0, 0.3, 0.4, 0.1, 0.0, 0.3]
#print(LGC(10,150))# a=3**7,M=2**8 b=7**3 [0.3, 0.4, 0.1, 0.0, 0.3, 0.4, 0.1, 0.0, 0.3, 0.4]
#print(LGC(100,516))

#x= [LGC(10000,166)]
""" a=2**9
    M=2^20-1 No da una distribución uniforme
    b=5**6
    """
x = [LGC(1000000,15)]
""" a=7**5
    M=2**31-1       Da distribución uniforme para todas las semillas
    b=0
    """
plt.hist(x)
plt.ticklabel_format(axis='y',style='sci')
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('x',fontsize=18)
plt.ylabel('Frecuencia',fontsize=18)
plt.title('a$=9$, M$=1103$, b=1, $10^6$ muestras',fontsize=18)
plt.show()
