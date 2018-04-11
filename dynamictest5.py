# Dynamic test
#https://www.todavianose.com/leer-el-puerto-serie-de-arduino-con-python-y-pyserial/
#https://matplotlib.org/examples/pylab_examples/polar_demo.html
#http://www.toptechboy.com/tutorial/python-with-arduino-lesson-11-plotting-and-graphing-live-data-from-arduino-with-matplotlib/
#!/usr/bin/python
# https://matplotlib.org/examples/pylab_examples/annotation_demo.html

# Importamos la libreira de PySerial
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import *
from drawnow import *

# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('COM9', 9600)

rr = np.zeros(181)
thstep = np.pi/181
thr = np.arange(0,np.pi,thstep)

rL = np.zeros(181)
thL = np.arange(np.pi,2*np.pi,thstep)


perim = 0
area = 0

nzrr = [] #los radios no nulos
nzthr = [] #los ángulos correspondientes a dichos radios
nzindexr = [] #los índices de elementos no nulos

nzrL = []
nzthL = []
nzindexL = []

plt.ion()

count = 0

def makeFig():
	######################

	axr = plt.subplot(111, projection='polar')
	axr.plot(nzthr, nzrr)
	axr.set_rlabel_position(-22.5) 
	axr.set_title("Mapa interior", va='bottom')
	######################

	axL = plt.subplot(111, projection='polar')
	axL.plot(nzthL, nzrL)
	######################
	maxr = max(nzrr)
	maxL = max(nzrL)
	maxmax = max(maxr,maxL)
	axr.set_rmax(maxmax)
	axr.set_rticks([0.25*maxmax, 0.5*maxmax, 0.75*maxmax, maxmax])  # less radial ticks

	###############################################################################################
	axr.annotate('Perímetro = ' + str (round(perim,2)) + '[$cm$] \nÁrea = ' + str(round(area,2)) + '[$cm^2$]',
            	xy=(np.pi/4, maxr),  # theta, radius
            	xytext=(0.76, 0.76),    # fraction, fraction
            	textcoords='figure fraction',
            	horizontalalignment='left',
            	verticalalignment='bottom')

def persurf(angR,distR,angL,distL): # Función para calcular perímetro y área, asume que no hay elementos nulos
	
	# Calcular perímetro
	arcsR = []
	arcsL = []

	surfsR = []
	surfsL = []

	# Lado derecho
	for i in range(1,len(angR)):
		# Extraer radios y ángulo
		aR = distR[i]
		bR = distR[i-1]
		rth = angR[i]-angR[i-1]

		# Calcular arco
		arclenR = np.sqrt( aR**2 + bR**2 - 2*aR*bR*np.cos(rth)) # Teorema del coseno
		arcsR.append(arclenR)

		# Calcular superficies
		surfR = (aR*bR*np.sin(rth))/2
		surfsR.append(surfR)

	# Lado izquierdo
	for i in range(1,len(angL)):
		# Extraer radios y ángulo
		aL = distL[i]
		bL = distL[i-1]
		Lth = angL[i]-angL[i-1]

		# Calcular arco
		arclenL = np.sqrt( aL**2 + bL**2 - 2*aL*bL*np.cos(Lth)) # Teorema del coseno
		arcsL.append(arclenL)

		# Calcular superficies
		surfL = (aL*bL*np.sin(Lth))/2
		surfsL.append(surfL)

	per = np.sum(arcsR) + np.sum(arcsL)
	surf = np.sum(surfsR) + np.sum(surfsL)

	ps = np.array([per , surf])
	return ps

def cleanplot():
	global rr
	global rL
	rr = np.zeros(181)
	rL = np.zeros(181)	

sleep(3) #Para esperar al arduino

while True:
	while (PuertoSerie.inWaiting()==0):
		pass
	# leemos hasta que encontarmos el final de linea
	sArduino = PuertoSerie.readline()
	leng = len(sArduino)
	sread = sArduino[0:leng-2]
	sread = str(sread)
	sread = sread[2:]

	# Mostramos el valor leido y eliminamos el salto de linea del final
	if (sread == 'clear'):
		cleanplot()

	else :
	# if count > 20:
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

		##### Extraer elementos no nulos #####
		nzindexr = np.nonzero(rr)
		nzindexL = np.nonzero(rL)

		nzrr = rr[nzindexr]
		nzthr = thr[nzindexr]

		nzrL = rL[nzindexL]
		nzthL = thL[nzindexL]

	##  Perímetro y área ###
	calcpa = persurf(nzthr,nzrr,nzthL,nzrL) # Calcular perímetro y área
	perim = calcpa[0]
	area = calcpa [1]

	### Graficar ###

	drawnow(makeFig)
	plt.pause(.000001)
	count += 1 
	if count>20:
		plt.clf()
		count=0
# ###########################################################

# print(rr)
# print(len(rr))
# print(thr)
# print (len(thr))
# print(rL)
# print(len(rL))
# print(thL)
# print(len(thL))