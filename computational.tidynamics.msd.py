#In this file, I compute mean square dispacemwnt via tidynamics
#To run the file, you need to type: python computational.tidynamics.msd.py Data.csv
import numpy as np
import tidynamics
import pandas as pd
import sys

if len(sys.argv)==2:
    output = sys.argv[1]

def main(number):
    #create zero numpy array with size n
    mean=np.linspace(0,0,number)

    #initial origin
    initialx_y=0

    for i in range(number):
        x_y=np.linspace(1.,20.,1000)

    #copy x_y to mean
    mean[:]=x_y

    #compute msd
    msd = tidynamics.msd(mean)

    #save data into csv file
    np.savetxt(output, msd)



if __name__=="__main__":
    main(1000)

