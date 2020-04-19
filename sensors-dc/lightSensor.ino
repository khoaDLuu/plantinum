
const int LDR_PIN = A5;

void setup () {
  Serial.begin(9600);
}

void loop () {
  int light = analogRead(LDR_PIN);
  Serial.print("Light intensity = ");
  Serial.println(light);
  delay(1000);
}
