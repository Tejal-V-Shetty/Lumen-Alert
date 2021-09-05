#include<Servo.h>
Servo mover;
int wled = 4, rled=3;
int moverpin = 10;
String dataset= "03000";
int angle=0, ledtype=0, ltype=0;
/*Dataset format
 * 123 - Angle (000 to 180)
 * 4 - LED Type (0-None, 1-White, 2-Red)
 * 5 - Light type (0-Off, 1-Steady light, 2-Blinking)
*/
void setup() {
  Serial.begin(9600);
  pinMode(wled,OUTPUT);
  pinMode(rled,OUTPUT);
  mover.attach(moverpin);
}

void loop() {
  if(Serial.available())
      dataset=Serial.readStringUntil('\n');
  angle= ((int)dataset[0]-48)*100+((int)dataset[1]-48)*10+((int)dataset[2]-48);
  ledtype= (int)dataset[3]-48;
  ltype= (int)dataset[4]-48;
  mover.write(angle);
  delay(100);
  if(ledtype==0)
  {
     digitalWrite(wled,LOW);
     digitalWrite(rled,LOW);
  }
  else
     if(ledtype==1&&ltype==1)//White wakelight
          digitalWrite(wled,HIGH);
     else
         if(ledtype==2&&ltype==2)
         {
            digitalWrite(rled,LOW);
            delay(50);
            digitalWrite(rled,HIGH);
         }
  delay(100);
}
