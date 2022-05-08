#include "DHT.h"

#define DHTPIN 8     // what digital pin we're connected to
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);
int speakerPin = 5;
int input_data;

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  float hif = dht.computeHeatIndex(f, h);
  float hic = dht.computeHeatIndex(t, h, false);

  while (Serial.available())
  {
    input_data = Serial.read();
  }

  Serial.print(t);
  Serial.print(" ");
  Serial.print(h);
  Serial.print("\n");

  if (input_data == '0')
  {
    tone(speakerPin, 300);
  }
  else if (input_data == '1')
  {
    noTone(speakerPin);
  }


}
