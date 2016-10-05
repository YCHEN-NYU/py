"""
Simple demo of the fill function.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rc


# title, x-axis label, y-axis label
titlename = r'$S_{12}-H_{//}$'

x1_labelname = r'$H_{//}(T)$'
y1_labelname = r'$S_{12}^{real}$'

x2_labelname = r'$H_{//}(T)$'
y2_labelname = r'$S_{12}^{imag}$'



fontLabel = 14
fontAxis = 24
fontTitle = 28
N = 4
colors = cm.rainbow(np.linspace(0,1,N))

x = np.linspace(-N, N,100)

fig = plt.figure(figsize=(8,6),facecolor="white")
ax = plt.subplot(111)
plt.hold(True)

for i in range(0,N):
    y = np.sin(np.pi*x+np.pi*i/2*np.linspace(1,1,100))*pow(x,2)
    plt.plot(y, x, color=colors[i], linewidth=5)
    # plt.plot(x, y, color=colors[i], linewidth=5)

# ax.set_xlim(-1, 1)
# ax.set_ylim(-1, 1)
# rc('font', size=fontAxis)
plt.axis('off')
# plt.xlabel('$x$', fontsize=fontAxis, fontweight='bold')
# plt.ylabel('$y$', fontsize=fontAxis, fontweight='bold')
# plt.title('$ y = f(x) $', fontsize=fontTitle, fontweight='bold')
plt.grid(False)
plt.hold(True)
plt.show()
fig.savefig('colorband.png')
