import time
from neopixel import *
import lib

strip = Adafruit_NeoPixel(lib.LED_COUNT, lib.LED_PIN, lib.LED_FREQ_HZ, lib.LED_DMA, lib.LED_INVERT, lib.LED_BRIGHTNESS, lib.LED_CHANNEL, lib.LED_STRIP)
strip.begin()
for i in range(strip.numPixels()): strip.setPixelColor(i, Color(0,0,0))
strip.show()
