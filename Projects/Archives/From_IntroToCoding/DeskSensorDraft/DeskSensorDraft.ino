/*
  Desk Sensor for Studying
  Brennon York
  4/20/2026
  byork8@my.gcu.edu or yorkbrennon7@gmail.com
*/

#include <Adafruit_CircuitPlayground.h>

bool FOCUS_MODE = false;
bool lastButtonState = false;

float baseline = 0;
float sensitivity = 1.5;

unsigned long COOLDOWN = 2000;
unsigned long lastAlertTime = 0;

void setPixels(uint8_t r, uint8_t g, uint8_t b, float brightness) {
  for (int i = 0; i < 10; i++) {
    CircuitPlayground.setPixelColor(i, r * brightness, g * brightness, b * brightness);
  }
}

float getBrightness() {
  float light = CircuitPlayground.lightSensor();
  float brightness = light / 1023.0;

  if (brightness < 0.1) brightness = 0.1;
  if (brightness > 0.8) brightness = 0.8;

  return brightness;
}

bool detectNoise() {

  int raw = CircuitPlayground.soundSensor();

  // Initialize baseline
  if (baseline == 0) {
    baseline = raw;
  }

  // Stronger smoothing = ignores quick spikes
  baseline = (baseline * 0.985) + (raw * 0.015);

  float deviation = raw - baseline;

  // Require sustained / stronger deviation
  float threshold = sensitivity * 12;

  // Optional: ignore tiny spikes completely
  if (deviation < 0) return false;

  if (deviation > threshold) {
    return true;
  }

  return false;
}

void alert() {
  unsigned long currentTime = millis();

  if (currentTime - lastAlertTime > COOLDOWN) {

    for (int i = 0; i < 3; i++) {
      setPixels(255, 0, 0, getBrightness());
      for (int i = 0; i < 5; i++) {
        CircuitPlayground.playTone(880, 50);
        delay(40);
      }

      delay(100);

      setPixels(0, 0, 0, 0);
      delay(100);
    }

    lastAlertTime = currentTime;
  }
}

void setup() {
  CircuitPlayground.begin();
}

void loop() {

  bool currentButtonState = CircuitPlayground.leftButton();

  if (currentButtonState && !lastButtonState) {
    FOCUS_MODE = !FOCUS_MODE;
  }

  lastButtonState = currentButtonState;

  float brightness = getBrightness();

  if (FOCUS_MODE) {

    setPixels(0, 255, 0, brightness);

    if (detectNoise()) {
      alert();
    }

  } else {
    setPixels(0, 0, 50, 0.2);
  }

  delay(20);
}