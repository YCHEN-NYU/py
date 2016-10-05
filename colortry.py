import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


N = 500
data1 = np.random.randn(N)
data2 = np.random.randn(N)
colors = np.linspace(0,1,N)

#plt.scatter(data1, data2, c=colors, cmap=cm.hsv)
plt.scatter( data1, data2, cmap=cm.hsv)

plt.colorbar()

plt.show()