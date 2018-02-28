import RPi.GPIO as GPIO
import time

LedPin = 11  # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.output(LedPin, GPIO.HIGH)

def blink(t):
	# while True:
	GPIO.output(LedPin, GPIO.HIGH)
	time.sleep(t)
	GPIO.output(LedPin, GPIO.LOW)
	time.sleep(t)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		for i in range(5):
			blink(0.5)
		[blink(1) for i in range(4)]

	except KeyboardInterrupt:
		destroy()
