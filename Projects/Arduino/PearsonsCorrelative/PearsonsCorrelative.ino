/*
  Pearson Correlation Coefficient Function
  Brennon York
  3/5/2026
  byork8@my.gcu.edu or yorkbrennon7@gmail.com
*/

#include <Wire.h>
#include <Adafruit_CircuitPlayground.h>
#include <Adafruit_Circuit_Playground.h>

const int sampleSize = 100;

float lightData[sampleSize];
float accelData[sampleSize];

int indexSample = 0;
unsigned long lastSampleTime = 0;


// Pearson Correlation Function
float pearsonCorrelation(float x[], float y[], int n)
{
  float sumX = 0;
  float sumY = 0;
  float sumXY = 0;
  float sumX2 = 0;
  float sumY2 = 0;

  for(int i = 0; i < n; i++)
  {
    sumX += x[i];
    sumY += y[i];
    sumXY += x[i] * y[i];
    sumX2 += x[i] * x[i];
    sumY2 += y[i] * y[i];
  }

  float numerator = (n * sumXY) - (sumX * sumY);
  float denominator = sqrt((n * sumX2 - sumX * sumX) * (n * sumY2 - sumY * sumY));

  if(denominator == 0)
    return 0;

  return numerator / denominator;
}


void setup()
{
  Serial.begin(115200); 
  CircuitPlayground.begin(); 
  Serial.println("System Ready");
}


void loop()
{
  if(millis() - lastSampleTime >= 50)
  {
    lastSampleTime = millis();

    float lightValue = CircuitPlayground.lightSensor();
    float accelZ = CircuitPlayground.motionZ();

    lightData[indexSample] = lightValue;
    accelData[indexSample] = accelZ;

    indexSample++;

    if(indexSample >= sampleSize)
    {
      float r = pearsonCorrelation(lightData, accelData, sampleSize);

      Serial.print("Correlation Coefficient: ");
      Serial.println(r, 4);

      indexSample = 0;
    }
  }
}