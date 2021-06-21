#in the file, I plot data from Data.csv in x axis and time in y axis.
#To run, you need to type python visualization.tidynamics.msd.py Data.csv msd.png


import pandas as pd
import matplotlib.pyplot as plt
import tidynamics
import csv
import sys
import numpy as np

if len(sys.argv)==3:
    input = sys.argv[1]
    output = sys.argv[2]


def main():

        #load data from saved csv file

    arr1 = pd.read_csv(input,header=None)


    mean = arr1
    time = np.arange(1000)[1:1000//2]
        #resize time axis to plot
    z=np.resize(time, (1000,1))

    #define figuresize
    plt.rcParams['figure.figsize']=(10,10)



    #plot data

    plt.plot(mean,z)
    plt.xlabel('mean square displacement')
    plt.ylabel('time')

    plt.title('Examples for the mean-square displacement',loc = 'left')
    plt.savefig(output, dpi=100, bbox_inches='tight')
    plt.show()



if __name__=="__main__":
    main()
