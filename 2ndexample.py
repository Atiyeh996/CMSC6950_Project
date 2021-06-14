import tidynamics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tidynamics


spacing = np.linspace(-5 * np.pi, 5 * np.pi, num=500)
s = pd.Series(0.7 * np.random.rand(500) + 0.3 * np.sin(spacing))
t= pd.Series(0.4 * np.random.rand(500) + 0.7 * np.sin(spacing))


acf = tidynamics.correlation(s,t)
plt.plot(acf)
plt.savefig('4.png', dpi=300, bbox_inches='tight')
plt.show()


