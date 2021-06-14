import sys
import tidynamics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tidynamics

if len(sys.argv)==2:
    output=sys.argv[1]

plt.style.use('ggplot') 
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
#compute tidynamics.correlation

def corr():
    spacing = np.linspace(-5 * np.pi, 5 * np.pi, num=500)
    s = pd.Series(0.7 * np.random.rand(500) + 0.3 * np.sin(spacing))
    t= pd.Series(0.4 * np.random.rand(500) + 0.7 * np.sin(spacing))


    acf = tidynamics.correlation(s,t)
    plt.plot(acf,marker='.',ms = 2, mfc = 'm',linestyle='dotted',linewidth = '2')
    
    plt.title("correlation over time",fontdict=font2,loc = 'right')
    plt.xlabel("correlation",fontdict=font1)
    plt.ylabel("time",fontdict=font1)
    
    plt.savefig(output, dpi=300, bbox_inches='tight')
    plt.show()

    return plt

corr()

