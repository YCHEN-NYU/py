import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(8, 8))
fig.patch.set_facecolor('white')


DeltaE = np.linspace(0, 1, 100)
Tf = DeltaE**(0.25)

plt.title(r'$\Delta E - T_f $')
plt.xlabel('$\Delta E$', fontsize = 20)
plt.ylabel('$T_f$', fontsize = 20)
plt.plot(DeltaE, Tf, linewidth = 2 )
plt.grid(True)
plt.show()