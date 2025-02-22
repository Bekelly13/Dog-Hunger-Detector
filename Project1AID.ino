int buzzerPin = 9;  // Set your buzzer pin here

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read();  // Read the serial input
    
    if (received == '1') {
      tone(buzzerPin, 1000);  // Emit a 1000 Hz tone on the buzzer
    } else if (received == '0') {
      noTone(buzzerPin);  // Stop the tone
    }
  }
}
