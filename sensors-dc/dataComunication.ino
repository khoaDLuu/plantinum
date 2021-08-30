#include <DHT.h>
#include <Servo.h>

const int LDR_PIN = A5;
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
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  int light = analogRead(LDR_PIN);
  int mois = analogRead(A0);
  
  if(!(isnan(t)) && !(isnan(h))) {
    Serial.println(temp);
    Serial.println(humi);
    Serial.println(light);
    Serial.println(mois);
  }
  else {
    // Error handling goes here...
  }

  if (moisture > 600) {
    myServo.write(SWITCH_ON);
  }
  else if (moisture < 500) {
    myServo.write(SWITCH_OFF);
  }
  
  delay(3000);
}
