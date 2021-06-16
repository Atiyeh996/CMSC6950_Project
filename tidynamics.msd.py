import array as arr
import matplotlib.pyplot as plt
import tidynamics
import random
import sys
from numpy import *

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.rcParams['figure.figsize']=(10,12)

plt.style.use('Solarize_Light2')



try:
    N=2000
    mean=linspace(0,0,N,dtype=float)
    count=0
    dock=range(1,100)
    for i in dock:
        s=[-1,1]
        steps=random.choice(s, size=(N,2))
        data = cumsum(steps, axis=0)
        mean += tidynamics.msd(data)
        count+=1


    mean /= count
    mean = mean[1:N//2]

    T = arange(1,N//2)

    plt.plot(T, mean,color="#444444",linestyle="--",marker = 'o',ms =5 ,linewidth = '1', label='Random walk (num.)')

    plt.plot(T, 2*T,color="r",linestyle="--",marker = 'o',ms =5,linewidth = '1', label='Random walk (theo.)')

    plt.plot(T[1:], tidynamics.msd(T)[1:],color="#bf00ff", marker='o', ms = 5,linewidth = '1',label='Constant velocity (num.)')
    plt.plot(T[1:], T[1:]**2,color="#eeb704", marker='o' ,ms = 5,linewidth = '1', label='Constant velocity (theo.)')

    plt.legend()
    plt.loglog()
    plt.plot()
    plt.xlabel('time', fontdict = font1, fontsize=10)
    plt.ylabel('mean square displacement',fontdict = font1, fontsize=10)
    plt.title('Examples for the mean-square displacement', fontdict = font2, fontsize=10, loc = 'left')
    plt.savefig("figure_msd.png", dpi=100, bbox_inches='tight')
    plt.show()

except:
    raise ValueError('bad value is supllied')

