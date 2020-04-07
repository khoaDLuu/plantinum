#include "DHT.h"            
const int DHTPIN = 4;      
const int DHTTYPE = DHT11;  
 
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  dht.begin();       
}
 
void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();    
 
  Serial.print("Nhiet do: ");
  Serial.println(t);               
  Serial.print("Do am: ");
  Serial.println(h);  
              
  Serial.println();               
  delay(1000);                     
}