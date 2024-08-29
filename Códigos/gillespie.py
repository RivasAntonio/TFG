import numpy as np
import matplotlib.pyplot as plot

def gillespie_SIS(infected, susceptible, recovery_rate, infecting_rate, tmax):
    time = np.array([0.])
    inf = np.array([infected]) #Creamos listas con los valores iniciales
    sus = np.array([susceptible])
    t = 0
    while t < tmax and inf[-1] > 0:
        print(t)
        r1 = infecting_rate * infected * susceptible / individuos #Probabilidad I+S---> I+I
        r2 = recovery_rate * infected #Probabilidad I----> S
        r_total = r1 + r2 # "Probabilidad total para normalizar la exponencial"
        delta_t = np.random.exponential(scale=1/r_total)#Le damos la media que deseamos a la escala temporal
        prob = np.random.rand() #Probabilidad uniforme de no infectarse
        if prob < r1/r_total: #Se produce infección
            infected += 1
            susceptible -= 1
        else: #Se produce recuperación
            infected -= 1
            susceptible += 1
        t += delta_t
        time=np.append(time,t)
        inf=np.append(inf,infected)
        sus=np.append(sus,susceptible)
    return time, inf, sus

# Damos valor a los parámetros
recovery_rate = 1
infecting_rate = 1
individuos = 100
infectados_inicio = individuos/10
susceptible_inicio = individuos - infectados_inicio


trayectorias = 3
for i in range(trayectorias):
    time, inf, sus = gillespie_SIS(infectados_inicio, susceptible_inicio, recovery_rate, infecting_rate+0.1*i, 100)
    print(infecting_rate+0.1*i)
    plot.plot(time, inf/individuos, label=f'$\lambda=$ %.2f' %(infecting_rate+0.1*i))
    #plot.plot(time,sus, label=f'Trayectoria susceptibles {i+1}')
plot.xlabel('Tiempo')
plot.ylabel('Individuos')
#plot.ylim(0,10000)
plot.legend()
plot.show()