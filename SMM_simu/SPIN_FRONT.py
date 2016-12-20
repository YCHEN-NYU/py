import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(8,6))
fig.patch.set_facecolor('white')

gz = 1.99
gx = 1.94
D = 0.708
muB = 0.67145
S = 10
TD = 38
PI = 3.1416
kB = 1
A = 234
alpha = 3
beta = 13/3

Hz = np.linspace(0,1,500)
Hx = np.linspace(0,4,500)

hz = gz*muB/(2*D*S)*Hz
hx = gx*muB/(2*D*S)*Hx

# Energy Barrier
U = D*S**2*(((1-hz)**2 -2*hx*np.sqrt(1-hz)/(1-hz)**2))

# Flame Temperatures
Tf = TD*((alpha+1)*gz*muB*S*Hz/(A*kB*TD))**(0.25)
factor = 0.5
Tf_reduced = Tf*factor;

h1 = plt.plot(Hz, Tf, 'b--', linewidth = 2, label = '$T_f$')
h2 = plt.plot(Hz, Tf_reduced, 'r--', linewidth = 2, label = '$0.5 T_f$')
plt.legend(loc='upper left')
plt.title('$Flame Temperature T_f - H_z$', fontsize = 20)
plt.xlabel('$H_z$', fontsize = 14)
plt.ylabel('$T_f (K)$', fontsize = 14)
plt.grid(True)
plt.show()
plt.close()
