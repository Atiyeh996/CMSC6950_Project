import sys
#import tidynamics
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
    return plt


corr()
