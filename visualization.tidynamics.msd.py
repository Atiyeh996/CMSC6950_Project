from matplotlib import pyplot as plt
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.rcParams['figure.figsize']=(10,10)
plt.plot(l, mean,color="#444444",linestyle="--",marker = 'o',ms =5 ,linewidth = '1', label='Random walk (num.)')
plt.plot(l, 2*l,color="r",linestyle="--",marker = 'o',ms =5,linewidth = '1', label='Random walk (theo.)')

plt.plot(l[1:], tidynamics.msd(l)[1:],color="#bf00ff", marker='o', ms = 5,linewidth = '1',label='Constant velocity (num.)')
plt.plot(l[1:], l[1:]**2,color="#eeb704", marker='o' ,ms = 5,linewidth = '1', label='Constant velocity (theo.)')

plt.legend()
plt.loglog()
plt.plot()
plt.xlabel('time', fontdict = font1, fontsize=10)
plt.ylabel('mean square displacement',fontdict = font1, fontsize=10)
plt.title('Examples for the mean-square displacement', fontdict = font2, fontsize=10, loc = 'left')
plt.savefig("output", dpi=100, bbox_inches='tight')
plt.show()
