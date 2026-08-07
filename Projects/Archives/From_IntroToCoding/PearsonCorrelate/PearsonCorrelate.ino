/*
  Pearson Correlation Coefficien
  Brennon York
  3/8/2026
  byork8@my.gcu.edu or yorkbrennon7@gmail.com
*/

#include <Wire.h>
#include <Adafruit_CircuitPlayground.h>

const int sampleSize = 100;
const int delayTime = 50;

float lightData[sampleSize];
float accelData[sampleSize];

int sampleIndex = 0;


/*
   FUNCTION: computePearson

   Parameters:
   x[] - first dataset
   y[] - second dataset
   n   - number of samples
*/
float computePearson(float x[], float y[], int n)
{
  float sumX = 0;
  float sumY = 0;
  float sumXY = 0;
  float sumX2 = 0;
  float sumY2 = 0;

  for (int i = 0; i < n; i++)
  {
    sumX += x[i];
    sumY += y[i];
    sumXY += x[i] * y[i];
    sumX2 += x[i] * x[i];
    sumY2 += y[i] * y[i];
  }

  float numerator = (n * sumXY) - (sumX * sumY);
  float denominator = sqrt((n * sumX2 - sumX * sumX) *
                           (n * sumY2 - sumY * sumY));

  if (denominator == 0)
    return 0;

  return numerator / denominator;
}


void setup()
{
  Serial.begin(9600);
  CircuitPlayground.begin();

  Serial.println("Starting correlation measurement...");
}


void loop()
{
  // Read sensors
  float lightValue = CircuitPlayground.lightSensor();
  float accelZ = CircuitPlayground.motionZ();

  // Store values
  lightData[sampleIndex] = lightValue;
  accelData[sampleIndex] = accelZ;
  sampleIndex++;

  if (sampleIndex >= sampleSize)
  {
    float correlation = computePearson(lightData, accelData, sampleSize);

    Serial.print("Pearson Correlation: ");
    Serial.println(correlation);

    sampleIndex = 0; // restart sampling
  }

  delay(delayTime);
}