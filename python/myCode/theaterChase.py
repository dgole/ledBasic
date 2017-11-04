import time
from neopixel import *
import lib

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()
while True:
	#lib.theaterChase(strip, Color(127, 127, 127))  # White theater chase
	lib.theaterChase(strip, Color(127,   0,   0))  # Red theater chase
	#lib.theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
	#lib.rainbow(strip)
	#lib.rainbowCycle(strip)
	#lib.theaterChaseRainbow(strip)
