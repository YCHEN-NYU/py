import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import cm
import os
# % matplotlib inline
# ===================

colortable = cm.hsv(np.linspace(0,1,10))
markertable = ['o', 's', 'v', '^', 'o', 's', 'v',
               '^', 'o', 's', 'v', '^', 'o', 's', 'v', '^']

# move to the target folder
path = '/Users/yiyi/Desktop/Final_v3/STT5440_2'
os.chdir(path)

# get filenames in the folder
fileformat = '_' + str(input("f (GHz) = ")) + '000MHz.dat'

# title, x-axis label, y-axis label
titlename = r'$S_{12}-H_{//}$'

x1_labelname = r'$H_{//}(T)$'
y1_labelname = r'$S_{12}^{real}$'

x2_labelname = r'$H_{//}(T)$'
y2_labelname = r'$S_{12}^{imag}$'



fontLabel = 14
fontAxis = 24
fontTitle = 28

# fig = plt.figure(figsize = (12, 10), facecolor='white')

i = 0
for file in os.listdir('.'):
    if file.endswith(fileformat):
        f = file
        # Load data files into x, y

        rawdata = []
        for line in open(f, 'r').readlines():
            rawdata.append(line.split())

        # remove 1st and last data point
        del rawdata[0]
        del rawdata[len(rawdata)-1]

        # 1 --> H, 6 --> S12_real, 7 --> S12_imag
        indexH = 1
        index_S12_real = 6
        index_S12_imag = 7

        H = []
        S12_real = []
        S12_imag = []

        for element in rawdata[:]:
            H.append(element[indexH])
            S12_real.append(element[index_S12_real])
            S12_imag.append(element[index_S12_imag])

        x = H
        y_real = S12_real
        y_imag = S12_imag

        # Plot out x-y
        # Three subplots sharing both x-axis but not y-axis
        # f = plt.figure(figsize = (12, 10), facecolor='white')

        f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=False)
        plt.figure(figsize = (12, 10), facecolor='white')
        ax1.plot(x, y_real, linestyle='-')
        ax2.plot(x, y_imag, linestyle='-')
        # rc('font', size=fontLabel)

        ax1.set_title(titlename, fontsize=fontTitle, fontweight='bold')

        # Fine-tune figure; make subplots close to each other and hide x ticks for
        # all but bottom plot.
        # f.subplots_adjust(hspace=0)
        # plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)


        # ax = fig.add_subplot(111)
        # lines = plt.plot(x, y, linestyle='-')
        # plt.setp(lines, color=colortable[i], linewidth=2.0)
        # plt.xlabel(x1_labelname, fontsize=fontAxis, fontweight='bold')
        # plt.ylabel(y2_labelname, fontsize=fontAxis, fontweight='bold')
        # plt.title(titlename, fontsize=fontTitle, fontweight='bold')

        xmin = round(float(min(x)), 2)
        xmax = round(float(max(x)), 2)

        ymin_real = float(min(y_real))
        ymax_real = float(max(y_real))

        # ymin_imag = float(min(y_imag))
        # ymax_imag = float(max(y_imag))

        ymin_imag = round(float(min(y_imag)), 4)
        ymax_imag = round(float(max(y_imag)), 4)
        extra_margin = 0.1

        ax1.set_xlim(xmin - (xmax - xmin)*extra_margin,
                     xmax + (xmax - xmin)*extra_margin)
        #
        ax1.set_ylim(ymin_real - (ymax_real - ymin_real)*extra_margin,
                     ymax_real + (ymax_real - ymin_real)*extra_margin)
        #
        ax2.set_ylim(ymin_imag - (ymax_imag - ymin_imag)*extra_margin,
                     ymax_imag + (ymax_imag - ymin_imag)*extra_margin)

        plt.grid(False)
        plt.hold(True)
        plt.show()

        i += 1

# *************************
# *************************

plt.show()
