import time
from neopixel import *
import lib

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()
while True:
	print ('Color wipe animations.')
	lib.colorWipe(strip, Color(255, 0, 0))  # Red wipe
	lib.colorWipe(strip, Color(0, 255, 0))  # Blue wipe
	lib.colorWipe(strip, Color(0, 0, 255))  # Green wipe
	print ('Theater chase animations.')
	lib.theaterChase(strip, Color(127, 127, 127))  # White theater chase
	lib.theaterChase(strip, Color(127,   0,   0))  # Red theater chase
	lib.theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
	print ('Rainbow animations.')
	lib.rainbow(strip)
	lib.rainbowCycle(strip)
	lib.theaterChaseRainbow(strip)
