#include <DHT.h>

const int DHT_PIN = 4;
const int DHT_TYPE = DHT11;
DHT dht(DHT11_PIN, DHT_TYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if(!(isnan(t)) && !(isnan(h))) {
    Serial.print("Temparature = ");
    Serial.println(t);
    Serial.print("Humidity = ");
    Serial.println(h);
  }

  Serial.println();
  delay(1000);
}
