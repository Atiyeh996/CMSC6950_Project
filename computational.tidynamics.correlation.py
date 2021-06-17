import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tidynamics
from tidynamics import acf


def corr():
    s=np.random.randn(500)
    t= np.random.randn(500)

    acf = tidynamics.correlation(s,t)

corr()


