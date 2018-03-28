"""
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0,20, 0.01)
r =r**2 + 30
maxr = max(r)
size = len(r)
thstep = np.pi/size
theta = np.arange(0,np.pi,thstep)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
#ax.grid(True)

r2 = np.arange(0,20, 0.01)
r2 =r2**2 + 10
maxr2 = max(r2)
size2 = len(r2)
th2step = np.pi/size2
theta2 = np.arange(np.pi,2*np.pi,th2step)
ax2 = plt.subplot(111, projection='polar')
ax2.plot(theta2, r2)
maxmax = max(maxr,maxr2)
ax.set_rmax(maxmax)
ax.set_rticks([0.25*maxmax, 0.5*maxmax, 0.75*maxmax, maxmax])  # less radial ticks

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()

r[100:200] = np.zeros(100)+100

ax.plot(theta, r)