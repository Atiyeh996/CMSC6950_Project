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

#generate 0 array with size 2000

try:
    N=2000
    mean=linspace(0,0,N,dtype=float)
    count=0
   #pick 100 numbers from mean
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

    plt.plot(T, mean,color="r",linestyle="--",marker = 'o',ms =5,linewidth = '1', label='Random walk (theo.)')



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

