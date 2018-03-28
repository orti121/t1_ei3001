# Merge test
#https://www.todavianose.com/leer-el-puerto-serie-de-arduino-con-python-y-pyserial/
#https://matplotlib.org/examples/pylab_examples/polar_demo.html

#!/usr/bin/python

# Importamos la libreira de PySerial
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import *

# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('COM9', 9600)

count = 0

rr = np.zeros(181)
thstep = np.pi/181
thr = np.arange(0,np.pi,thstep)

rL = np.zeros(181)
thL = np.arange(np.pi,2*np.pi,thstep)

sleep(3) #Para esperar al arduino

while count<=380:
	# leemos hasta que encontarmos el final de linea
	sArduino = PuertoSerie.readline()
	leng = len(sArduino)
	sread = sArduino[0:leng-2]
	sread = str(sread)
	sread = sread[2:]

	# Mostramos el valor leido y eliminamos el salto de linea del final

	if count > 20:
		dR,dL,ths = sread.split(' , ')
		lth = len(ths)
		ths = ths[0:lth-1]
		dR = float(dR) # Convertimos los valores a número
		dL = float(dL) 
		th = int(ths)

		# print (sread) #prints para debuggear
		# print (dR)
		# print (dL)
		# print (th)
		rr[th] = dR
		rL[th] = dL
	count += 1  #para desechar la primera vuelta
# ###########################################################

# print(rr)
# print(len(rr))
# print(thr)
# print (len(thr))
# print(rL)
# print(len(rL))
# print(thL)
# print(len(thL))
maxr = max(rr)
axr = plt.subplot(111, projection='polar')
axr.plot(thr, rr)
axr.set_rlabel_position(-22.5)  # get radial labels away from plotted line
#ax.grid(True)

maxL = max(rL)
axL = plt.subplot(111, projection='polar')
axL.plot(thL, rL)
maxmax = max(maxr,maxL)
axr.set_rmax(maxmax)
axr.set_rticks([0.25*maxmax, 0.5*maxmax, 0.75*maxmax, maxmax])  # less radial ticks

axr.set_title("Mapa interior", va='bottom')
plt.show()