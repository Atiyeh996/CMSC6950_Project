# this file gives an input file (numbers1.csv) and save the output to acf.csv
#for running this file you need to type : python computational.tidynamics.acf.py numbers1.csv acf.csv



import matplotlib.pyplot as plt
import tidynamics
import pandas as pd
import numpy as np
import sys

if len(sys.argv)==3:
    input = sys.argv[1]
    output = sys.argv[2]


def main():

    #convert input file to pd
    file=pd.read_csv(input, names=['date','numbers'] , sep=",") 

    #create empty pd file for output
    file2 = pd.DataFrame()

    #define columns in input file
    z=file.iloc[:,0]
    zz=file.iloc[:,2]

    #compute tidynamics.acf for specific column 
    for i in file:
        af=tidynamics.acf(zz)

    #save acf to empty pd 
    file2[""]=af
    #convert file2 to csvfile with out index
    file2.to_csv(output,index=False) 



if __name__=="__main__":
    main()
