import matplotlib.pyplot as plt
from matplotlib import cm 
import numpy as np



N = 5;
x = np.linspace(-1,1,100)
colors = cm.hsv(np.linspace(0,1,N+1))

def format_axes(ax):
    ax.margins(0.2)
    ax.set_axis_off()
    
plt.close("all")
   
fig = plt.figure()

ax = plt.subplots()

for i in range(0,N):
    y = pow(x,i+1)
    plt.plot(x,y,color = colors[i],linestyle = '-', linewidth = 5)

ax = fig.add_subplot(111)
plt.hold(True)
        lines = plt.plot(x,y)
        plt.setp(lines, color= colors[i], linewidth=2.0)

        plt.title(titlename,fontsize = 18)
        plt.xlabel(xlabelname,fontsize = 12)
        plt.ylabel(ylabelname,fontsize = 12)
        
        xmin = round(float(min(x)),2)
        xmax = round(float(max(x)),2)
        ymin = round(float(min(y)),4)
        ymax = round(float(max(y)),4)
        
        ax.set_xlim(xmin+0.1,xmax*0.2)
        ax.set_ylim(ymin-(ymax-ymin)*0.5,ymax+(ymax-ymin)*0.5)
        #ax.annotate(r'$x-y$', xy=(xmax*0.1, ymax-(ymax-ymin)*0.1))
        i = i + 1
        
        ax = fig.add_subplot(111)
        plt.hold(True)plt.show()



    

