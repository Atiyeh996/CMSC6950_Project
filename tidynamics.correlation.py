import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tidynamics
from tidynamics import acf

def corr():
    spacing = np.linspace(-5 * np.pi, 5 * np.pi, num=500)
    s = pd.Series(0.6 * np.random.rand(500) + 0.3 * np.sin(spacing))
    t= pd.Series(0.4 * np.random.rand(500) + 0.7 * np.sin(spacing))
    acf = tidynamics.correlation(s,t)


    plt.style.use('ggplot') 
    font1 = {'family':'serif','color':'blue','size':20} 
    font2 = {'family':'serif','color':'darkred','size':15}



    plt.plot(acf,marker='.',ms = 2, mfc = 'm',linestyle='dotted',linewidth = '2')

    plt.title("correlation over time",fontdict=font2,loc = 'right')
    plt.xlabel("correlation",fontdict=font1)
    plt.ylabel("time",fontdict=font1)

    plt.savefig("figure_correlaion.png", dpi=100, bbox_inches='tight')
    plt.show()
corr()
