#include "DHT.h"
#define DHTPIN 8     // what digital pin we're connected to
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

#define         MG_PIN                       (A0)     
#define         BOOL_PIN                     (2)
#define         DC_GAIN                      (8.5)   

#define         READ_SAMPLE_INTERVAL         (50)    
#define         READ_SAMPLE_TIMES            (5)     
                                                     
#define         ZERO_POINT_VOLTAGE           (0.220) 
#define         REACTION_VOLTGAE             (0.030) 

float           CO2Curve[3]  =  {2.602,ZERO_POINT_VOLTAGE,(REACTION_VOLTGAE/(2.602-3))};

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(BOOL_PIN, INPUT);
  digitalWrite(BOOL_PIN, HIGH);
}

void loop() {
  
  int percentage;
  float volts;
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);

  volts = MGRead(MG_PIN);
  percentage = MGGetPercentage(volts,CO2Curve);

  if (percentage == -1) {
      Serial.print("400");
  } else {
      Serial.print(percentage);
  }
  Serial.print(" ");
 
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  float hif = dht.computeHeatIndex(f, h);
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(t);
  Serial.print(" ");
  Serial.print(h);
  Serial.print(" ");
  Serial.print("\n");

  delay(1000);
}

float MGRead(int mg_pin)
{
    int i;
    float v=0;

    for (i=0;i<READ_SAMPLE_TIMES;i++) {
        v += analogRead(mg_pin);
        delay(READ_SAMPLE_INTERVAL);
    }
    v = (v/READ_SAMPLE_TIMES) *5/1024 ;
    return v;
}

int  MGGetPercentage(float volts, float *pcurve)
{
   if ((volts/DC_GAIN )>=ZERO_POINT_VOLTAGE) {
      return -1;
   } else {
      return pow(10, ((volts/DC_GAIN)-pcurve[1])/pcurve[2]+pcurve[0]);
   }
}
