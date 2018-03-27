#!/usr/bin/python

# Importamos la libreira de PySerial
import serial

# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('COM9', 9600)
# Creamos un buble sin fin
while True:
  # leemos hasta que encontarmos el final de linea
  sArduino = PuertoSerie.readline()
  # Mostramos el valor leido y eliminamos el salto de linea del final
  #datalist = sArduino.split(",")
  #dR = datalist[0]
  #th = datalist[1]
  #dR = float(dR)
  #th = float(th)
  print (sArduino)
  #print (dR)
  #print (th)