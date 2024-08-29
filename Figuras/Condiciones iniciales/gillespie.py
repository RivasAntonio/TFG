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
    return time, inf
# Damos valor a los parámetros
recovery_rate = 1
infecting_rate = 2
individuos = 1000
#infectados_inicio = individuos/10
#susceptible_inicio = individuos - infectados_inicio

#Gráficas ni vs t para varias CCII

trayectorias = 5
for i in range(trayectorias):
    infectados_inicio=int(individuos*(0.1+0.2*i))
    susceptible_inicio = individuos - infectados_inicio
    time, inf = gillespie_SIS(infectados_inicio, recovery_rate, infecting_rate, 50)
    plot.plot(time, inf/individuos, label=f'$n_0/N=$ %.2f' %(infectados_inicio/individuos))
    print(infectados_inicio)


plot.ylabel('$n_i/N$',fontsize=16)
plot.xlabel('t',fontsize=16)  

plot.ylim([0,1.175])

plot.yticks(np.arange(0,1.2,0.2),fontsize=17)
plot.xticks(np.arange(0,60,10),fontsize=17)

plot.legend(loc='upper right',fontsize=14)

plot.title('$N=%d$ '%(individuos),fontsize=18)
plot.show()


#Aquí hacemos la gráfica ni vs lambda

"""infectados_inicio=int(individuos/10)
trayectorias = 40
medias=np.array([]) #Vector que contendrá las medias
inf_rates=np.array([])#Vector que contendrá los lambdas
for i in range(trayectorias):
    time, inf= gillespie_SIS(infectados_inicio, recovery_rate, 0.+0.075*i,100)
    #plot.plot(time, inf/individuos, label=f'$\lambda=$ %.2f' %(0.+0.5*i))
    inf_est=np.array(inf[int(np.ceil(np.size(inf)/2)):np.size(inf):1])#Crea un vector con la mitad de valores de infectados
    medias=np.append(medias,[np.mean(inf_est)/individuos]) #Media normalizada
    inf_rates=np.append(inf_rates,0.+0.075*i)
    print(np.size(medias))

plot.plot(inf_rates,medias,'-')
plot.ylabel('$\dfrac{<n_i>}{N}$')
plot.ylim([0,1])
#plot.legend(loc='upper left')
plot.xlabel('$\lambda$')                #Obtenemos la gráfica n_i vs lambda
plot.title('$N=%d$'%(individuos))
plot.show()"""