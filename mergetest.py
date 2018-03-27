# Merge test
#https://www.todavianose.com/leer-el-puerto-serie-de-arduino-con-python-y-pyserial/
#https://matplotlib.org/examples/pylab_examples/polar_demo.html

#!/usr/bin/python

# Importamos la libreira de PySerial
import serial
import numpy as np
import matplotlib.pyplot as plt

# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('COM9', 9600)
# Creamos un buble sin fin
while True:
  # leemos hasta que encontarmos el final de linea
  sArduino = PuertoSerie.readline()
  # Mostramos el valor leido y eliminamos el salto de linea del final
  dR = float(sArduino[5:9]) #extrae la distancia medida
  print (sArduino)




r = np.zeros(360)
size = len(r)
thstep = 2*np.pi/size
theta = np.arange(0,2*np.pi,thstep)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
#ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()