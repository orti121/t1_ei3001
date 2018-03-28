"""
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0,20, 0.01)
r =r**2
maxr = max(r)
size = len(r)
thstep = 2*np.pi/size
theta = np.arange(0,2*np.pi,thstep)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(maxr)
ax.set_rticks([0.25*maxr, 0.5*maxr, 0.75*maxr, maxr])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
#ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()