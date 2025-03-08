int buzzerPin = 9;  // Buzzer connected to pin 9
int ledPin = 8;     // LED connected to pin 8

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read();  // Read the serial input
    
    if (received == '1') {
      tone(buzzerPin, 1000);   // Turn on buzzer at 1000 Hz
      digitalWrite(ledPin, LOW); // Turn off LED
    } 
    else if (received == '0') {
      noTone(buzzerPin);        // Turn off buzzer
      digitalWrite(ledPin, HIGH); // Turn on LED
    }
  }
}

