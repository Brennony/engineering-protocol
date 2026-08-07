/*
  Desk Sensor Code
  Brennon York
  4/17/2026
  byork8@my.gcu.edu or yorkbrennon7@gmail.com
*/

#include <Adafruit_CircuitPlayground.h>

/* -------------------------------
   CONFIGURATION VARIABLES
   ------------------------------- */

bool FOCUS_MODE = false;          // Tracks whether focus mode is ON or OFF
int NOISE_THRESHOLD = 200;        // Sound level needed to trigger alert (adjust as needed)
unsigned long COOLDOWN = 2000;    // Minimum time between alerts (milliseconds)
unsigned long lastAlertTime = 0;  // Stores last time an alert was triggered


/* -------------------------------
   HELPER FUNCTION: SET PIXELS
   Controls all 10 NeoPixels on the Circuit Playground
   ------------------------------- */
void setPixels(uint8_t r, uint8_t g, uint8_t b, float brightness) {

  for (int i = 0; i < 10; i++) {
    CircuitPlayground.setPixelColor(
      i,
      r * brightness,
      g * brightness,
      b * brightness
    );
  }
}


/* -------------------------------
   HELPER FUNCTION: GET BRIGHTNESS
   Uses built-in light sensor to auto-adjust LED brightness
   ------------------------------- */
float getBrightness() {

  float light = CircuitPlayground.lightSensor(); // Reads ambient light (0–1023)

  // Normalize brightness to usable range
  float brightness = light / 1023.0;

  // Clamp brightness so LEDs are always visible
  if (brightness < 0.1) brightness = 0.1;
  if (brightness > 0.8) brightness = 0.8;

  return brightness;
}


/* -------------------------------
   HELPER FUNCTION: ALERT SYSTEM
   Triggered when noise exceeds threshold
   Includes cooldown to prevent spam alerts
   ------------------------------- */
void alert() {

  unsigned long currentTime = millis();

  // Check cooldown timer
  if (currentTime - lastAlertTime > COOLDOWN) {

    // Flash red LEDs + sound alert 3 times
    for (int i = 0; i < 3; i++) {

      // RED warning flash
      setPixels(255, 0, 0, getBrightness());

      // Sound alert
      CircuitPlayground.playTone(880, 100);

      delay(100);

      // Turn LEDs off briefly
      setPixels(0, 0, 0, 0);

      delay(100);
    }

    // Update last alert time
    lastAlertTime = currentTime;
  }
}


/* -------------------------------
   SETUP FUNCTION (RUNS ONCE)
   Initializes hardware
   ------------------------------- */
void setup() {

  CircuitPlayground.begin();
}


/* -------------------------------
   MAIN LOOP (RUNS FOREVER)
   Handles input, sensors, and output
   ------------------------------- */
void loop() {

  /* ---------------------------
     TOUCH INPUT (TOGGLE MODE)
     --------------------------- */

  // Touch pad A1 toggles focus mode
  if (CircuitPlayground.capTouch(1) > 1000) {

    FOCUS_MODE = !FOCUS_MODE;

    // Debounce delay to prevent multiple triggers
    delay(500);
  }


  // Get current brightness based on room lighting
  float brightness = getBrightness();


  /* ---------------------------
     FOCUS MODE ACTIVE
     --------------------------- */
  if (FOCUS_MODE) {

    // Green indicates focus mode is active
    setPixels(0, 255, 0, brightness);

    // Read ambient sound level
    int soundLevel = CircuitPlayground.soundSensor();

    // If sound exceeds threshold, trigger alert
    if (soundLevel > NOISE_THRESHOLD) {
      alert();
    }
  }


  /* ---------------------------
     IDLE MODE (NOT FOCUSED)
     --------------------------- */
  else {

    // Dim blue indicates standby mode
    setPixels(0, 0, 50, 0.2);
  }


  // Small delay to stabilize loop and reduce sensor noise
  delay(50);
}