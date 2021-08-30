const int MS_PIN = A0;

void setup() {
  ​Serial.begin(9600);
  // ​pinMode(MS_PIN, INPUT);
}

void loop() {
  // Read the voltage value from A0
  ​// The value is in the range from 0 to 1023
  ​int moisture = analogRead(A0);
  ​Serial.println(value);
  ​delay(10);
}
