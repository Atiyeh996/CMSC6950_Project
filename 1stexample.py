import array as arr
import matplotlib.pyplot as plt
import tidynamics
import random
from numpy import *



mean=linspace(0,0,1000,dtype=float)
count=0

dock=range(1,33)
for i in dock:
    s=[-1,1]
    steps=random.choice(s, size=(1000,2))
    data = cumsum(steps, axis=0)
    mean += tidynamics.msd(data)
    count+=1


mean /= count
mean = mean[1:1000//2]

l = arange(1,500)

plt.plot(l, mean, label='Random walk (num.)')

plt.plot(l, 2*l, label='Random walk (theo.)')

plt.plot(l[1:], tidynamics.msd(l)[1:],label='Constant velocity (num.)', ls='--')
plt.plot(l[1:], l[1:]**2,label='Constant velocity (theo.)', ls='--')


plt.loglog()
plt.legend()
plt.xlabel('time')
plt.ylabel('mean square displacement')
plt.title('Examples for the mean-square displacement')
plt.savefig('2.png', dpi=100, bbox_inches='tight')


plt.show()


