import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse
# %matplotlib inline

NUM = 500

ells = [Ellipse(xy=rnd.rand(2)*30, width=rnd.rand(),
                height=rnd.rand(), angle=rnd.rand()*360)
        for i in range(NUM)]

fig = plt.figure( figsize=(10.8, 19.2), facecolor='w', )
ax = fig.add_subplot(111, aspect='equal')
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(rnd.rand())
    e.set_facecolor(rnd.rand(3))

ax.set_xlim(0, 10.8)
ax.set_ylim(0, 19.2)
plt.axis('off')
plt.show()
fig.savefig('foo.png')