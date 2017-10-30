import time
from neopixel import *
import lib
import numpy as np


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()

def setPixelsWithArray(strip, a):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(int(a[i,0]), int(a[i,1]), int(a[i,2])))
	strip.show()

def normalizeArray(a):
	return 255 * a/np.amax(a)
	
a = np.zeros([strip.numPixels(), 3])
center = 30
width  = 5
for i in range(center-width, center+width+1):
	distance = np.absolute(i-center)
	distanceNorm = float(distance)/float(width)
	a[i,0] = 1.0 - distanceNorm
a = np.square(a)
a = normalizeArray(a)

plusOrMinus = 1
while True:
	if center == 59 or center == 0: plusOrMinus*=-1
	a = np.roll(a, plusOrMinus, axis=0)
	setPixelsWithArray(strip, a)
	time.sleep(0.1)
	center+=plusOrMinus	
