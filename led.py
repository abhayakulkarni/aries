import neopixel
from rpi_ws281x import Color, PixelStrip
import time
import board
 
pixel_pin = board.D18
num_pixels = 8
# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53


ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write = False, pixel_order = ORDER)


def colorWipe(strip, color, wait_ms=50):
	for i in range(strip.numpixels):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def chasing(strip, color, wait_ms=500, iterations=1000):
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
	  			strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms / 1000.0)
			for i in range(0, strip.numPixels(), 3):
		 		strip.setPixelColor(i+q, 0)

def fadeinout():
	for y in range(0,255):
		for x in range(0,LED_COUNT):
			strip.setPixelColor(x, Color(255,255,0))
			strip.setBrightness(y)
			strip.show()

def slowblink(color,wait):
	pixels.fill(color)
	pixels.show()
	time.sleep(wait)
	pixels.fill((0,0,0))
	pixels.show()
	time.sleep(wait) 
 
def fastpulsing(color,wait):
	pixels.fill(color)
	pixels.show()
	time.sleep(wait)
	pixels.fill((0,0,0))
	pixels.show()
	time.sleep(wait)



if __name__ == '__main__':
	strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
	strip.begin()
	print('Press ctl-C to quit.')
	while True:

		#green chasing 
#		chasing(strip, Color(0,255,0))
#		for i in range(0,LED_COUNT):	
#			colorWipe(strip, Color(0,255,0))
#			time.sleep(3)
#		time.sleep(30)	
	
		#yellow chasing
#		chasing(strip, Color(255,255,0))
#		for i in range(0, LED_COUNT):
#			colorWipe(strip, Color(255,255,0))
#		time.sleep(30)

		#yellow fadeinout		
#		for i in range (1000):
#			fadeinout()
#			i = i+1  
#			strip.setBrightness(0)
#		time.sleep(30)			
		
	

	#purple slow pulsing 	
#		for blinks in range(1000):
#			slowblink((128,0,128), 1)
#		time.sleep(30)

		#red fast pulsing
		for blinks in range(100000):
			fastpulsing((0,255,0), 0.2)
		time.sleep(30)
		#blue fast pulsing
		for blinks in range(1000):
			fastpulsing((0,0,255), 0.2)

		time.sleep(30)
		#green slow blinking
		for blink in range(5):
			fastpulsing((255,0,0),1)
 
