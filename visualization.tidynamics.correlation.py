import tidynamics
from tidynamics import acf
import sys
from matplotlib import pyplot as plt

plt.style.use('ggplot') 
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#if len(sys.argv)==2:
 #
#   output=sys.argv[1]

plt.plot(acf,marker='.',ms = 2, mfc = 'm',linestyle='dotted',linewidth = '2')

plt.title("correlation over time",fontdict=font2,loc = 'right')
plt.xlabel("correlation",fontdict=font1)
plt.ylabel("time",fontdict=font1)

plt.savefig("correlation.py", dpi=300, bbox_inches='tight')
plt.show()
#return plt
