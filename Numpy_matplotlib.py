#pip install numpy
#pip install matplotlib

import numpy as np

np.array([1, 2, 3])

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
    
    
import matplotlib.pyplot as plt
import datetime
import numpy as np

xs = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(24)])
ys = np.random.randint(100, size=xs.shape)
zs = np.random.randint(100, size=xs.shape)

# Plot one series:
plt.plot(xs, ys)
plt.show()

# Plot two series:
plt.plot(xs, ys, "", xs, zs, "") ## two lines on same chart, "" to separate two lines
plt.show()
