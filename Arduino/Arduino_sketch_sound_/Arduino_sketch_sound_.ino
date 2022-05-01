int input_data;

int speakerPin = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //  pinMode(5, OUTPUT);
  //  digitalWrite(12,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
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
