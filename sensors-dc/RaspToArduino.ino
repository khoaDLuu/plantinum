int data;
void setup() {
    Serial.begin(9600);
}
void loop() {
    data = Serial.read();
    Serial.print(data);
    delay(1000);
}