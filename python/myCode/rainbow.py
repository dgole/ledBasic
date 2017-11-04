import time
from neopixel import *
import lib

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()
while True:
	lib.rainbowCycle(strip, wait_ms=20, iterations=5)
