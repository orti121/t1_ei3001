#!/usr/bin/python

# Importamos la libreira de PySerial
import serial

# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('COM9', 9600)
# Creamos un buble sin fin
while True:
  # leemos hasta que encontarmos el final de linea
  sArduino = PuertoSerie.readline()
  leng = len(sArduino)
  sread = sArduino[0:leng-2]
  sread = str(sread)
  sread = sread[2:]
  
  # Mostramos el valor leido y eliminamos el salto de linea del final
  
  dR,dL,th = sread.split(' , ')
  lth = len(th)
  th = th[0:lth-1]

  dR = float(dR) # Convertimos los valores a número
  dL = float(dL) 
  th = int(th)

  #print (sread)
  print (dR)
  #print (dL)
  #print (th)