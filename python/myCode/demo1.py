import time
from neopixel import *
import lib
import numpy

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()

def setPixelsWithArray(strip, a):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(a[i,0], a[i,1], a[i,2]))
	strip.show()

while True:
	a = numpy.zeros([strip.numPixels(), 3])
	for n in range(0, strip.numPixels()):
		a[0:n, 0] = n * (strip.numPixels()/255)
		setPixelsWithArray(strip, a)
