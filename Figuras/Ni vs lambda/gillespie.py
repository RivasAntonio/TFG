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


medias=np.array([]) #Vector que contendrá las medias
inf_rates=np.array([])#Vector que contendrá los lambdas
recovery_rate = 1
#infecting_rate = 1.5
#individuos = 100
#infectados_inicio = individuos/10
#susceptible_inicio = individuos - infectados_inicio


trayectorias = 40
for j in range (3):
    medias=np.array([]) #Vector que contendrá las medias
    inf_rates=np.array([])#Vector que contendrá los lambdas
    desviacion=np.array([])
    individuos = 10**(j+1)
    infectados_inicio = individuos/10
    tmax = 100
    for i in range(trayectorias):
        time, inf= gillespie_SIS(infectados_inicio, recovery_rate, 0.+0.125*i,tmax)
        inf_est=np.array(inf[int(np.ceil(np.size(inf)/2)):np.size(inf):1])#Crea un vector con la mitad de valores de infectados
        medias=np.append(medias,[np.mean(inf_est)/individuos]) #Media normalizada
        #desviacion=np.append(desviacion,[np.std(inf_est)/individuos])
        inf_rates=np.append(inf_rates,0.+0.125*i)
        print(np.size(inf_rates))
    plot.plot(inf_rates,medias,'-', label='N=%d'%(individuos))
    #plot.plot(inf_rates,desviacion,'-', label='N=%d'%(individuos)) 
    #plot.errorbar(inf_rates, medias, yerr=desviacion, label='N=%d'%(individuos), fmt = '-', ecolor='k', capsize=3, capthick=1)   
  
plot.ylabel('$<n_i>/N$',fontsize=16)
plot.xlabel('$\lambda$',fontsize=16)  

plot.ylim([-0.1,1])

plot.yticks(np.arange(0,1.2,0.2),fontsize=17)
plot.xticks(np.arange(0,6,1),fontsize=17)

plot.legend(loc='upper left',fontsize=14)

#plot.title('$N=%d$ '%(individuos),fontsize=18)
plot.show()