import array as arr
import matplotlib.pyplot as plt
import tidynamics
import random
from numpy import * 
try:
    N=2000
    mean=linspace(0,0,N,dtype=float)
    count=0
    dock=range(1,50)
    for i in dock:
        s=[-1,1]
        steps=random.choice(s, size=(N,2))
        data = cumsum(steps, axis=0)
        mean += tidynamics.msd(data)
        count+=1


    mean /= count
    mean = mean[1:N//2]

    T = arange(1,N//2)


except:
    raise ValueError('bad value is supllied')




