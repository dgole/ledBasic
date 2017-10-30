import time
from neopixel import *
import lib
import numpy

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()

frame=0
while True:
	rval = frame % 255
	for i in range(lib.LED_COUNT):
		strip.setPixelColor(i, Color(rval, 0, 0))
	strip.show()
	frame+=1
