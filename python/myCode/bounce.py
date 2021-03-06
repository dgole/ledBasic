import time
from neopixel import *
import lib
import numpy as np

strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()

a = np.zeros([strip.numPixels(), 3])
center = 30
width  = 5
for i in range(center-width, center+width+1):
	distance = np.absolute(i-center)
	distanceNorm = float(distance)/float(width)
	a[i,0] = 1.0 - distanceNorm + 0.2
a = np.square(a)
a = lib.normalizeArray255(a)

plusOrMinus = 1
while True:
	if center == 59-width or center == 0+width: plusOrMinus*=-1
	a = np.roll(a, plusOrMinus, axis=0)
	lib.setPixelsWithArray(strip, a)
	center+=plusOrMinus	
	time.sleep(0.05)
