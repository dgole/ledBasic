import time
from neopixel import *
import lib
import sys

c1 = int(sys.argv[1])
c2 = int(sys.argv[2])
c3 = int(sys.argv[3])

strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()

for i in range(strip.numPixels()): strip.setPixelColor(i, Color(c1,c2,c3))

strip.show()
