/*
  Responding to Sensory Input
  Brennon York
  February 5, 2026
  byork8@my.gcu.edu or yorkbrennon7@gmail.com

  Using your Arduino and its built-in temperature sensor and speaker, 
  you will be building a virtual "cricket" that chirps at the same 
  rate as an actual cricket.
*/

// Libraries
#include <Adafruit_CircuitPlayground.h>
#include <Adafruit_Circuit_Playground.h>

void setup() 
{
    Serial.begin(115200);
    while(!Serial);
    Serial.println("==Program Start==");
    
    CircuitPlayground.begin();
}

void loop() 
{
  // Measure temp
  float tempC = CircuitPlayground.temperature();

  // Convert to F (if needed) 
  float tempF = ((1.8 * tempC) + 32);

  // Convert F to chirpMin
  int numChirpsMin = (((tempF - 50) * 4) + 40);
  
  // Convert chirpMin to delay
    // I used a float since I was able to get it to work with a simple math change
  float chirpDelay = (60000 / numChirpsMin);
  Serial.print("chirp delay is: ");
  Serial.print(chirpDelay);
  Serial.println(" msec");
  delay(1000);

  // Sound chirp
  CircuitPlayground.playTone(2150, 200);

  // Delay chirpDelay
  delay(chirpDelay);
}
