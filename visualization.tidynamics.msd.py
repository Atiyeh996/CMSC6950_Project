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
    try:
        #load data from saved csv file

        arr1 = pd.read_csv(input,header=None)


        N=100
        #extract data  from file
        mean = arr1[1:N//2]
        #convert dataframe to numpy array
        new=mean.to_numpy()




        time = np.arange(N)[1:N//2]
        #resize time axis to plot
        z=np.resize(time, (49,1))
        #define figuresize

        plt.rcParams['figure.figsize']=(10,10)

        #plot data

        plt.plot(new,z,color="#444444",linestyle="--",marker = 'o',ms =5 ,linewidth = '1', label='Walk')


        plt.title('Examples for the mean-square displacement',loc = 'left')
        plt.savefig(output, dpi=100, bbox_inches='tight')
        plt.show()


    except:
        pass
if __name__=="__main__":
    main()
