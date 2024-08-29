import numpy as np
import matplotlib.pyplot as plot
import time 

def gillespie_SIS(infected, susceptible, recovery_rate, infecting_rate, tmax):
    time = np.array([0.])
    inf = np.array([infected]) #Creamos listas con los valores iniciales
    sus = np.array([susceptible])
    t = 0
    pesos=np.empty(1)

   
    while (t < tmax) and (infected > 0):     
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
        pesos=np.append(pesos,delta_t)
        if infected ==0:
            infected += 1
            susceptible -=1
    return time, inf, sus, pesos

# Damos valor a los parámetros
recovery_rate = 1
infecting_rate = 1
individuos = 100
infectados_inicio = individuos/10
susceptible_inicio = individuos - infectados_inicio

#Aquí hacemos la gráfica lambda vs n_i

trayectorias = 1
medias_pond=np.array([]) #Vector que contendrá las medias
inf_rates=np.array([])#Vector que contendrá los lambdas
for i in range(trayectorias):
    time, inf, sus, pesos = gillespie_SIS(infectados_inicio, susceptible_inicio, recovery_rate, infecting_rate+0.1*i,100)
    plot.plot(time, inf/individuos, label=f'$\lambda=$ %.2f' %(infecting_rate+0.1*i))
    inf_est=np.array(inf[int(np.ceil(np.size(inf)/2)):np.size(inf):1])#Crea un vector con la mitad de valores de infectados
    pesos_est=np.array(pesos[int(np.ceil(np.size(inf)/2)):np.size(inf):1]) #Crea un vector con los pesos en el estacionario
    inf_pesados=np.multiply(inf_est,pesos_est)
    medias_pond=np.append(medias_pond,np.sum(inf_pesados)/np.sum(pesos_est)/individuos) #Media ponderada normalizada
    inf_rates=np.append(inf_rates,infecting_rate+0.1*i)
    print(np.size(medias_pond))
plot.ylim([0,1])
plot.xlabel('Tiempo')
plot.ylabel('Individuos')
plot.title('N=%d, $\mu=1$ paso 0.1'%(individuos))           #Con esta parte obtenemos gráfica n_i vs t
#plot.legend()
plot.show()

"""plot.plot(inf_rates,medias_pond,'-')
plot.ylabel('$< n_i>$')
plot.xlabel('$\lambda$')                #Obtenemos la gráfica n_i vs lambda
plot.title('$N=100$, $\mu=1$, 40 días')
plot.show()"""