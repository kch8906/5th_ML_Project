int speakerPin = 5;
int input_data;

void setup() {
  Serial.begin(9600);

}

void loop() {

  while (Serial.available())
  {
    input_data = Serial.read();
  }

  if (input_data == '0')
  {
    tone(speakerPin, 300);
  }
  else if (input_data == '1')
  {
    noTone(speakerPin);
  }


}
