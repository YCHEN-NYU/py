import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rc
import numpy as np
# % matplotlib inline
# curve colors
N = 5
colors = cm.hsv(np.linspace(0, 1, N + 1))
LabelX = '$x$'
LabelY = '$y$'
TitleName = LabelY + '$-$' + LabelX

fontAxis = 20
fontLegend = 20
fontTitle = 24

fig = plt.figure(figsize=(8, 6))
fig.patch.set_facecolor('white')
ax = plt.subplot(111)

xmin = 0.01
xmax = 1
NumofPoints = 1000

x = np.linspace(xmin, xmax, NumofPoints)
y = x*np.exp(-1/x)

plt.semilogy(x, y, color=colors[0], linestyle='-', linewidth=2)


fig.subplots_adjust(right=1.0)
formula = r"$y=xe^{-\frac{1}{x}}$"
ax.text(0.45, 0.45, formula, transform=ax.transAxes, fontsize=20)
ax.set_xlim(xmin, xmax)
# ax.set_ylim(0, 1)
rc('font', size=fontAxis)
plt.axis('on')
plt.xlabel(LabelX, fontsize=fontAxis, fontweight='bold')
plt.ylabel(LabelY, fontsize=fontAxis, fontweight='bold')
plt.title(TitleName, fontsize=fontTitle, fontweight='bold')
plt.grid(True)
plt.hold(True)
# fig.savefig('fx.png')
plt.show()
