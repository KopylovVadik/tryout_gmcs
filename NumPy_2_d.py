import math

import numpy as np
from matplotlib import pylab as plt

x = np.linspace(0, math.pi * 2, num=100, endpoint=True)

y = np.sin(x)
z = np.cos(x)

plt.grid()
plt.plot(x, y)
plt.plot(x, z)

plt.show()
