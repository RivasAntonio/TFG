import numpy as np
import matplotlib.pyplot as plot

def focker_planck(deltat,x_0,individuos,infecting_rate,recovery_rate,tmax):
    t=0.
    time = np.array([0.])
    x = np.array([x_0])
    sqrtdeltat=np.sqrt(deltat)
    while t < tmax:
        f = x[-1] + deltat*(infecting_rate*x[-1]*(1-x[-1])-recovery_rate*x[-1])+sqrtdeltat*np.sqrt(np.abs(infecting_rate*x[-1]*(1-x[-1])+recovery_rate*x[-1])/individuos)*np.random.normal()
        if f<0:
            f=1/individuos
        x = np.append(x,f)
        t += deltat
        time = np.append(time,t)
    return x, time

deltat=0.1
x_0=0.1
individuos=1000
infecting_rate=2
recovery_rate=1
tmax=100

##########################################################################################################################
"""x vs t"""
##########################################################################################################################
trayectorias=5
for j in range(trayectorias) :
        infecting_rate = 0.5+0.5*j
        x , time = focker_planck(deltat,x_0,individuos,infecting_rate,recovery_rate,tmax)
        plot.plot(time, x,'-',label=f"$\lambda= %.2f$"%(infecting_rate))
    
plot.ylabel('$n_i/N$',fontsize=16)
plot.xlabel('$t$',fontsize=16)
plot.title('$\mu=1.00$, $N=1000$, $n_i(0)=N/10$',fontsize=18)
plot.legend(loc='upper left',fontsize=14)
plot.show()

##########################################################################################################################
"""x  vs lambda"""
##########################################################################################################################

"""
puntos = 40
for j in range (3):
    medias=np.array([]) #Vector que contendrá las medias
    inf_rates=np.array([])#Vector que contendrá los lambdas
    desviacion=np.array([])
    individuos = 10**(j+1)
    infectados_inicio = individuos/10
    tmax = 100
    for i in range(puntos):
        x, time= focker_planck(deltat,x_0,individuos,0.+0.125*i,recovery_rate,tmax)
        inf_est=np.array(x[int(np.ceil(np.size(x)/2)):np.size(x):1])#Crea un vector con la mitad de valores de infectados
        medias=np.append(medias,[np.mean(inf_est)]) #Media normalizada
        desviacion=np.append(desviacion,[np.std(inf_est)])
        inf_rates=np.append(inf_rates,0.+0.125*i)
        print(np.size(medias))
    plot.plot(inf_rates,medias,'-', label='N=%d'%(individuos))
    #plot.plot(inf_rates,desviacion,'-', label='N=%d'%(individuos)) 
    #plot.errorbar(inf_rates, medias, yerr=desviacion, label='N=%d'%(individuos), fmt = '-', ecolor='k', capsize=3, capthick=1)  


plot.ylabel('$<x>$',fontsize=16)
plot.xlabel('$\lambda$',fontsize=16)  

plot.ylim([-0.1,1])

plot.yticks(np.arange(0,1.2,0.2),fontsize=17)
plot.xticks(np.arange(0,6,1),fontsize=17)

plot.legend(loc='upper left',fontsize=14)

#plot.title('$N=%d$ '%(individuos),fontsize=18)
plot.show()"""