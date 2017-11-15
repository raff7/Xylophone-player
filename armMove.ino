//paramether to tune
int BETWEEN_NOTES_DELAY = 100;
int treshold = 10;
int minMovment= 5;


#include <Servo.h>
int motorPin1 = 33;
int motorPin2 = 32;
int motorPin3 = 31;
Servo servo1;
Servo servo2;
Servo servo3;
int s3Angle0 = 102;
int s2Angle0 = 87;
int s1Angle0 = 92;

int previousMillis = 0;
int intervall = 5;
int delta1 = 0;
int delta2 = -3;
int delta3 = 10;
void setup() {
  // put your setup code here, to run once:
  servo1.attach(motorPin1);
  servo1.write(s1Angle0);
  servo2.attach(motorPin2);
  servo2.write(s2Angle0+45);
  servo3.attach(motorPin3);
  servo3.write(s3Angle0+45);

  Serial.begin(9600);

}
void hit(){
        double pre1 = servo1.read();
        double pre2 = servo2.read();
        double pre3 = servo3.read();

        servo1.write(servo1.read()+delta1);
        servo2.write(servo2.read()+delta2);
        servo3.write(servo3.read()+delta3);
       delay(100);
        servo1.write(pre1);
        servo2.write(pre2);
        servo3.write(pre3);
}
void moveToAngle(int angle1,int angle2,int angle3){
  servo1.write(s1Angle0-angle1);
  servo2.write(s2Angle0-angle2);
  servo3.write(s3Angle0+angle3); 
}
void approachAngle(int angle1,int angle2,int angle3){
  int t1 = angle1;
  int t2 = angle2;
  int t3 = angle3;
  int a1 = servo1.read();
  int a2 = servo2.read();
  int a3 = servo3.read();
  int d = pow(a1-t1,2)+pow(a2-t2,2)+pow(a3-t3,2);
  while(d>treshold){
    int temp;
    if(a1>t1){
      temp = min(minMovment,a1-t1);
      servo1.write(a1-temp);
      a1 = a1-temp;
    }if(t1>a1){
      temp = min(minMovment,t1-a1);
      servo1.write(a1+temp);
      a1 = a1+temp;
    }if(a2>t2){
      temp = min(minMovment,a2-t2);
      servo2.write(a2-temp);
      a2 = a2-temp;
    }if(t2>a2){
      temp = min(minMovment,t2-a2);
      servo2.write(a2+temp);
      a2 = a2+temp;
    }if(a3>t3){
      temp = min(minMovment,a3-t3);
      servo3.write(a3-temp);
      a3 = a3-temp;
    }if(t3>a3){
      temp = min(minMovment,t3-a3);
      servo3.write(a3+temp);
      a3 = a3+temp;
    }  
    d = pow(a1-t1,2)+pow(a2-t2,2)+pow(a3-t3,2);
  }

}
void playNote(int a1,int a2,int a3,int t){
  moveToAngle(a1,a2,a3);
  delay(100);
  hit();
  delay(max(t-BETWEEN_NOTES_DELAY,100));

}
void readInput() {
    if (Serial.available()) {
      String type = Serial.readStringUntil(' ');
      if(type == "angles"){// example: 'angles 0 0 0' to hit on starting position.
         int angle1 =(int) Serial.readStringUntil(' ').toInt();
         int angle2 =(int) Serial.readStringUntil(' ').toInt();
         int angle3 =(int)  Serial.readStringUntil('\n').toInt();
         moveToAngle(angle1,angle2,angle3);     
         delay(100);
         hit();
     }
     if(type == "melody"){
      int a1= Serial.readStringUntil(' ').toInt();
      int a2= Serial.readStringUntil(' ').toInt();
      int a3= Serial.readStringUntil(' ').toInt();
      int t= Serial.readStringUntil(';').toInt();
      playNote(a1,a2,a3,t);
      while(a1 != NULL){
        int a1= Serial.readStringUntil(' ').toInt();
        int a2= Serial.readStringUntil(' ').toInt();
        int a3= Serial.readStringUntil(' ').toInt();
        int t= Serial.readStringUntil(';').toInt();
        playNote(a1,a2,a3,t);
      }
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
