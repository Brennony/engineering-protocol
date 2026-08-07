/*
  Recording Data
  Brennon York
  February 3, 2026
  byork8@my.gcu.edu or yorkbrennon7@gmail.com

  What do we want to do:
    Obtain 100 samples from the light sample with 100 milisecond delays
    Moving average with 10 samples
    Plot the moving average on the serial plotter
    Try different window sizes and observe the differences
*/

// Libraries
#include <Adafruit_CircuitPlayground.h>

// Make global vars
byte windSize = 20;
int dataArr[100];

void setup() 
{
  // Serial Port + Being Sensor
  Serial.begin(115200);
  while(!Serial);
  Serial.println("==Program Start==");
  CircuitPlayground.begin();

  // For loop, 0=99 data points
  for(int i = 0; i < 100; i++)
  {
    // Collect light value
    dataArr[i] = CircuitPlayground.lightSensor();
    // If state i greater than 0
    if(i > windSize-2)
    {
      // Take moving average
      float movAvg = 0.0f;
      int sum = 0;
      for(int j = i; j > (i - windSize); j--)
      {
        sum = sum + dataArr[j];
        movAvg = sum / windSize;
      }
      // Plot moving average
      Serial.println(movAvg);
      delay(100);
    }
  }
}

void loop()
{
  // No loops needed
}
