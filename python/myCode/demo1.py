import time
from neopixel import *
import lib
import numpy

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()

while True:
	for n in range(0, 60):
		a = numpy.zeros(lib.LED_COUNT,3)
		a[0:n, 0] = 255  
		for i in range(lib.LED_COUNT):
			strip.setPixelColor(i, Color(a[i,0],a[i,1],a[i,2]))
		strip.show()
		
