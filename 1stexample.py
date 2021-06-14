import array as arr
import matplotlib.pyplot as plt
import tidynamics
import random
from numpy import *

plt.rcParams['figure.figsize']=(10,10)
plt.rcParams['font.family'] = 'sans-serif'
#plt.rcParams['font.sans-serif'] = ['Tahoma']
plt.style.use('Solarize_Light2')
if __name__ == "__main__":
    N=2000
    mean=linspace(0,0,N,dtype=float)
    count=0
    dock=range(1,50)
    for i in dock:
        s=[-1,1]
        steps=random.choice(s, size=(N,2))
        data = cumsum(steps, axis=0)
        mean += tidynamics.msd(data)
        count+=1


    mean /= count
    mean = mean[1:N//2]

    l = arange(1,N//2)

    plt.plot(l, mean,color="#444444",linestyle="--", label='Random walk (num.)')

    plt.plot(l, 2*l,color="k",linestyle="--", label='Random walk (theo.)')

    plt.plot(l[1:], tidynamics.msd(l)[1:],color="#bf00ff", marker=',',label='Constant velocity (num.)', ls='--')
    plt.plot(l[1:], l[1:]**2,color="#eeb704", marker=',' , label='Constant velocity (theo.)', ls='--')

    plt.legend()
    plt.loglog()
    plt.plot()
    plt.xlabel('***time***')
    plt.ylabel('***mean square displacement***')
    plt.title('Examples for the mean-square displacement', fontsize=10)
    plt.savefig('3.png', dpi=100, bbox_inches='tight')
    plt.show()


