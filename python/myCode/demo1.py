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

a = np.zeros([strip.numPixels(), 3])
center = 30
width  = 5
for i in range(center-width, center+width+1):
	distance = np.absolute(i-center)
	distanceNorm = distance/width
	a[i] = 255 - (distanceNorm*255)
print(a)
a = np.square(a)
print(a)
	
frame = 0
while True:
	setPixelsWithArray(strip, np.roll(a, frame))
	frame+=1
