#include <DHT.h>
#include <Servo.h>
// use a struct variable to pack data

const int LDR_PIN = A5;
const int DHT11_PIN = 7;
const int DHT_TYPE = DHT11;
DHT dht(DHT11_PIN, DHT_TYPE);
Servo servo;
const int SERVO_PIN = 8;

void setup() {
  Serial.begin(9600);
  dht.begin();
  servo.attach(SERVO_PIN);
  servo.write(10);
}

void loop()
{
  int angle;
   // scan from 0 to 180 degrees
  for (angle = 10; angle < 170; angle++)
  {
    servo.write(angle);
    delay(15);
  }
  // now scan back from 180 to 0 degrees
  for (angle = 170; angle > 10; angle--)
  {
    servo.write(angle);
    delay(15);
  }

  float t = dht.readTemperature();
  float h = dht.readHumidity();
  int light = analogRead(LDR_PIN);
  if(!(isnan(t)) && !(isnan(h))) {
    Serial.println(t);
    Serial.println(h);
    Serial.println(light);
  }
  delay(1000);
}
