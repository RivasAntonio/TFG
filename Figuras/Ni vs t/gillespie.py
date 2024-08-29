import numpy as np
import matplotlib.pyplot as plot

def gillespie_SIS(infected, recovery_rate, infecting_rate, tmax):
    time = np.array([0.])
    inf = np.array([infected]) #Creamos listas con los valores iniciales
    t = 0
    while t < tmax and inf[-1] > 0:     
        r1 = infecting_rate * infected * (individuos-infected) / individuos #Probabilidad I+S---> I+I
        r2 = recovery_rate * infected   #Probabilidad I----> S
        r_total = r1 + r2 # "Probabilidad total para normalizar la exponencial"
        delta_t = np.random.exponential(scale=1/r_total)#Le damos la media que deseamos a la escala temporal
        prob = np.random.rand() #Probabilidad uniforme de no infectarse
        if prob < r1/r_total: #Se produce infección
            infected += 1
        else: #Se produce recuperación
            infected -= 1
            if infected == 0:
                infected +=1
        t += delta_t
        time=np.append(time,t)
        inf=np.append(inf,infected)
        print(t)
    return time, inf
# Damos valor a los parámetros
recovery_rate = 1
#infecting_rate = 0.1
individuos = 10000
infectados_inicio = individuos/10

trayectorias = 5
for i in range(trayectorias):
    infecting_rate=0.5+i*0.5
    time, inf = gillespie_SIS(infectados_inicio, recovery_rate, infecting_rate, 50)
    plot.plot(time, inf/individuos, label='$\lambda=$%.2f'%(infecting_rate))
    print(i+1)

plot.ylabel('$n_i/N$',fontsize=16)
plot.xlabel('t',fontsize=16)  

plot.ylim([0,1.175])

plot.yticks(np.arange(0,1.2,0.2),fontsize=17)
plot.xticks(np.arange(0,60,10),fontsize=17)

plot.legend(loc='upper left',fontsize=14)

plot.title('$N=%d$ '%(individuos),fontsize=18)
plot.show()
