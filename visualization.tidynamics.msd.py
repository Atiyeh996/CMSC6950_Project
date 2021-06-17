
from numpy import *
from matplotlib import pyplot as plt

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

    

plt.rcParams['figure.figsize']=(10,12)
plt.plot(T, mean,color="#444444",linestyle="--",marker = 'o',ms =5 ,linewidth = '1', label='Random walk (num.)')
plt.plot(T, 2*T,color="r",linestyle="--",marker = 'o',ms =5,linewidth = '1', label='Random walk (theo.)')


plt.legend()
plt.loglog()
plt.plot()
plt.xlabel('time', fontdict = font1, fontsize=10)
plt.ylabel('mean square displacement',fontdict = font1, fontsize=10)
plt.title('Examples for the mean-square displacement', fontdict = font2, fontsize=10, loc = 'left')
plt.savefig("figure_msd.png", dpi=100, bbox_inches='tight')
plt.show()


 
