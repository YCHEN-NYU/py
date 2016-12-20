import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rc
import numpy as np
# % matplotlib inline
# curve colors
N = 5
colors = cm.hsv(np.linspace(0, 1, N + 1))
LabelX = '$H_x$'
LabelY = '$U(H_z, H_x)$'
TitleName = LabelY + '$-$' + LabelX

fontAxis = 16
fontLegend = 16
fontTitle = 20

fig = plt.figure(figsize=(8, 6))
fig.patch.set_facecolor('white')
ax = plt.subplot(111)

Hzmin = 0
Hzmax = 1.2
Hxmin = 2
Hxmax = 4
NumofPoints = 100
# Hz = np.linspace(Hzmin, Hzmax, NumofPoints)
Hx = np.linspace(Hxmin, Hxmax, NumofPoints)
gz = 1.99
gx = 1.94
muB = 0.67145 # K/T
D = 0.708
S = 10

for i in range(1, 6):
    Hz = i*0.2
    hz = Hz*gz*muB/(2*D*S)
    hx = Hx*gx*muB/(2*D*S)
    U = D*S**2*(1-hz)**2*(1-2*hx*np.sqrt(1-hz**2)/(1-hz)**2)
    plt.plot(Hx, U, color=colors[i], linestyle='-', linewidth=2, label="$H_z={0}$".format(Hz))

fig.subplots_adjust(right=0.8)
plt.legend(loc="right", bbox_to_anchor=[1.25, 0.5],
           ncol=1, shadow=True, title="Legend", fancybox=True)
ax.set_xlim(Hxmin, Hxmax)
ax.set_ylim(0, 45)
rc('font', size=fontAxis)
plt.xlabel(LabelX, fontsize=fontAxis, fontweight='bold')
plt.ylabel(LabelY, fontsize=fontAxis, fontweight='bold')
plt.title(TitleName, fontsize=fontTitle, fontweight='bold')
plt.grid(True)
plt.hold(True)
fig.savefig('U_Hx.png')
plt.show()
