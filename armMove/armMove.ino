//paramether to tune
int approachingDelay = 1;
int Mspeed = 9;
int treshold = Mspeed;


#include <Servo.h>
int motorPin1 = 33;
int motorPin2 = 32;
int motorPin3 = 31;
Servo servo1;
Servo servo2;
Servo servo3;
double s3Angle0 = 85;
double s2Angle0 = 87;
double s1Angle0 = 92;

int previousMillis = 0;
int intervall = 10;
double delta1 = 0;
double delta2 = -3;
double delta3 = 7;
void setup() {
  // put your setup code here, to run once:
  servo1.attach(motorPin1);
  servo1.write(s1Angle0);
  servo2.attach(motorPin2);
  servo2.write(s2Angle0);
  servo3.attach(motorPin3);
  servo3.write(s3Angle0);

  Serial.begin(9600);

}
void bow(){
   
}
void hit(double a1, double a2,double a3){

        servo1.write(servo1.read()+delta1);
        servo2.write(servo2.read()+delta2);
        servo3.write(servo3.read()+delta3);
        delay(100);
        moveToAngle(a1,a2,a3);
}
void moveToAngle(double angle1,double angle2,double angle3){
  servo1.write(s1Angle0-angle1);
  servo2.write(s2Angle0-angle2);
  servo3.write(s3Angle0+angle3);
}


void approachAngle(float a1,float a2, float a3){
  
  int _delay=70;
  double phase[] = {0.3,0.50,1};
  float d1 = a1-(s1Angle0-servo1.read());
  float d2 = a2-(s2Angle0-servo2.read());
  float d3 = a3-(servo3.read()-s3Angle0);
  if(d1>0 or d2>0 or d3>0){
    for(int i=0;i<sizeof(phase)/sizeof(phase[0]);i++){
      float d1 = a1-(s1Angle0-servo1.read());
      float d2 = a2-(s2Angle0-servo2.read());
      float d3 = a3-(servo3.read()-s3Angle0);
      float s1d = (-d1)*phase[i];
      float s2d = (-d2)*phase[i];
      float s3d = (d3)*phase[i];
      servo1.write(servo1.read()+s1d);
      servo2.write(servo2.read()+s2d);
      servo3.write(servo3.read()+s3d);
      delay(_delay);
    }
  }
  //moveToAngle(a1,a2,a3);
}
void playNote2(double a1,double a2,double a3,int t){
  int timer = millis();
  approachAngle(a1,a2,a3);
  while(millis()-timer < t){
    delay(1);
  }
  hit(a1,a2,a3);

}
void playNote(double a1,double a2,double a3,int t){}
//  int timer = millis();
//  moveToAngle(a1,a2,a3);
//  while(millis()-timer < t){
//    delay(1);
//  }
//  hit(a1,a2,a3);
//    delay(100);
//}
void readInput() {
    if (Serial.available()) {
      String type = Serial.readStringUntil(':');
      if(type == "angles"){// example: 'angles 0 0 0' to hit on starting position.
         double angle1 = Serial.readStringUntil(' ').toInt();
         double angle2 = Serial.readStringUntil(' ').toInt();
         double angle3 = Serial.readStringUntil('\n').toInt();
         playNote(angle1,angle2,angle3,0);
     }if(type == "angles2"){// example: 'angles 0 0 0' to hit on starting position.
         double angle1 = Serial.readStringUntil(' ').toInt();
         double angle2 = Serial.readStringUntil(' ').toInt();
         double angle3 = Serial.readStringUntil('\n').toInt();
         playNote2(angle1,angle2,angle3,0);
     }
     if(type == "melody"){

      double a1 = NULL;
      double a2 = NULL;
      double a3 = NULL;
      int t = NULL;
      do{
        a1= Serial.readStringUntil(',').toInt();
        a2= Serial.readStringUntil(',').toInt();
        a3= Serial.readStringUntil(',').toInt();
        t= Serial.readStringUntil(';').toInt();
        Serial.println(a1);
        Serial.println(a2);
        Serial.println(a3);
        playNote2(a1,a2,a3,t);
      }while(Serial.available()>0);
     }
     if(type == "getPos"){
      String s = ("1: "+(String)(s1Angle0-servo1.read())+" 2: "+(String)(s2Angle0-servo2.read())+" 3: "+(String)(servo3.read()-s3Angle0));
      Serial.println(s);
     }
    }
}
void loop() {
  unsigned long currentMills = millis();
  if((currentMills - previousMillis) > intervall){
    readInput();
    previousMillis = currentMills;
  }
    
} 
