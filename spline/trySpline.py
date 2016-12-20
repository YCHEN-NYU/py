import numpy as np 
import matplotlib.pyplot as plt

tmesh1 = np.linspace(-2, 0, 100)
tmesh2 = np.linspace(0, 2, 100)

s1 = (tmesh1+1)**2 -1 
s2 = 1- (tmesh2-1)**2
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y')
plt.plot(tmesh1, s1, 'b--')
plt.hold(True)
plt.plot(tmesh2, s2, 'r--')
plt.show()