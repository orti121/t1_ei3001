/*
 Controlling a servo position using a potentiometer (variable resistor)
 by Michal Rinott <http://people.interaction-ivrea.it/m.rinott>

 modified on 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Knob
*/

/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

//Control de sensor de ultrasonido extraído de https://create.arduino.cc/projecthub/josemanu/medir-distancias-con-hc-sr04-63f81e


#include <Servo.h>
#define trigL 3//Trigger sensor izquierdo
#define echoL 5//Echo
//#define powL  //Alimentación

#define trigR 12
#define echoR 13
#define powR 11
#define servopin 9 //Pin del servomotor
#define del 250 //Milisegndos de retardo entre medidas
#define vccpot A5
#define gndpot A1
#define potpin A3  // analog pin used to connect the potentiometer
#define offset 0 //Offset de distancia de acuerdo a la distancia entre los sensores y el origen del sistema

Servo myservo;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position
long tiempo;
float distL;
float distR;    // variable para guardar la distancia medida
int val;    // variable to read the value from the analog pin


void setup() {
   
  pinMode(trigL, OUTPUT);
  pinMode(echoL, INPUT);
  //pinMode(powL, OUTPUT);
  //digitalWrite(powL,HIGH);
  
  //
  pinMode(vccpot, OUTPUT);
  pinMode(gndpot, OUTPUT);
  pinMode(potpin, INPUT);
  digitalWrite(vccpot, LOW);
  digitalWrite(gndpot, HIGH);
  
  //
  pinMode(trigR, OUTPUT);
  pinMode(echoR, INPUT);
  pinMode(powR, OUTPUT);
  digitalWrite(powR,HIGH);
  myservo.attach(servopin);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  myservo.write(pos);
}

void loop() {
    val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
    pos = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
    myservo.write(pos);              // tell servo to go to position in variable 'pos'    
    delay(del);                       // waits 15ms for the servo to reach the position
    distL = getdist(trigL,echoL);  //Para cuando haya dos sensores
    distR = getdist(trigR,echoR);   //Obtener la distancia medida por el US
    //distL = distR;                  //Por mientras
    Serial.print(distR + offset);
    Serial.print(" , ");
    Serial.print(distL + offset);
    Serial.print(" , ");
    Serial.println(pos);
}

float getdist(int trigpin, int echopin){
  float dist;
    // lanzamos un pequeño pulso para activar el sensor
  digitalWrite(trigpin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigpin, LOW);
  
  // medimos el pulso de respuesta
  tiempo = (pulseIn(echopin, HIGH)/2); // dividido por 2 por que es el 
                                       // tiempo que el sonido tarda
                                       // en ir y en volver
  // ahora calcularemos la distancia en cm
  // sabiendo que el espacio es igual a la velocidad por el tiempo
  // y que la velocidad del sonido es de 343m/s y que el tiempo lo 
  // tenemos en millonesimas de segundo
  dist = float(tiempo * 0.0343);  
  return dist;
}

