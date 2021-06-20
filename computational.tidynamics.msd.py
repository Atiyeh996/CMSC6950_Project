import numpy as np
import tidynamics
import pandas as pd




def main(number):
    #create zero numpy array with size n
    mean=np.linspace(0,0,number)

    #set steps
    list =([1,1],[-1,-1],[1,-1],[-1,1])

    #convert list to np array
    s=np.array(list)
  
    #resize array
    z=np.resize(s,(number,2))
   
    #compute tidynamics.msd
    mean +=tidynamics.msd(z)

    #save data into csv file
    np.savetxt('Data.csv', mean)



if __name__=="__main__":
    main(1000)

