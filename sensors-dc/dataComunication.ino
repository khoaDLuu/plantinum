#include <DHT.h>
#include <Servo.h>
/*
 * use a struct variable to pack data
 * and then send to the RPi
 */

const int LDR_PIN = A5;
//dht DHT;
const int DHT11_PIN = 7;
const int DHT_TYPE = DHT11;
const int SERVO_PIN = 8;
const int SWITCH_OFF = 30;
const int SWITCH_ON = 120;
DHT dht(DHT11_PIN, DHT_TYPE);
Servo myServo;

void setup() {
  Serial.begin(9600);
  dht.begin();
  myServo.attach(SERVO_PIN);
  myServo.write(SWITCH_OFF);
}

void loop() {
//  int chk = DHT.read11(DHT11_PIN);
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  int light = analogRead(LDR_PIN);
  int mois = analogRead(A0);
  
  // print out the value you read:
  
  if(!(isnan(t)) && !(isnan(h))) {
    
    Serial.println(temp);
    Serial.println(humi);
    Serial.println(light);
    Serial.println(mois);
  }
  else {
    Serial.print("Error... t = ");
    Serial.print(t);
    Serial.print("; h = ");
    Serial.println(h);
  }

  if (moisture > 600) {
    myServo.write(SWITCH_ON);
  }
  else if (moisture < 500) {
    myServo.write(SWITCH_OFF);
  }
  
  delay(3000);
}
