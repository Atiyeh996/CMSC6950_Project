#for this file, I use acf.csv from computaional.tidynamics.acf.py and two different time series time.csv and time2.csv
#to run the file you need to type: python visualization.tidynamics.acf.py acf1.csv time.txt time2.txt acf1.png

import sys
import tidynamics
from matplotlib.cbook import get_sample_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation


if len(sys.argv)==5:
    input1=sys.argv[1]
    input2=sys.argv[2]
    input3=sys.argv[3]
    output=sys.argv[4]


def main():
    #convert csv files to pd
    x = pd.read_csv(input1)
    y = pd.read_csv(input2)
    z = pd.read_csv(input3)

    #start making figures with two rows and one column

    fig, (ax1, ax2) = plt.subplots(2,1, constrained_layout=True, sharey=False)
   
    #plot first figure with acf.csv and time.csv
    ax1.plot(x, y, 'g--', linewidth='0.5')
    ax1.set_title('acf over time')
    ax1.set_xlabel('acf')
    ax1.set_ylabel('time')
 
    #plot second figure with acf.csv and time2.csv
    ax2.plot(x, z, 'r-.',linewidth='0.5')
    ax2.set_xlabel('acf')
    ax2.set_ylabel('time2')
    ax2.set_title('acf over time2')



    #make title for image
    fig.suptitle('Acf over two period of time', fontsize=16)



    #save figures 
    plt.savefig(output, dpi=100, bbox_inches='tight')







if __name__=="__main__":
    main()  
