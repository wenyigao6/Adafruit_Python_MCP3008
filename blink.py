import RPi.GPIO as GPIO
import time

LedPin = 11  # pin11




def setup():
	GPIO.setmode(GPIO.BOARD)
	
	# GPIO.output(LedPin, GPIO.HIGH)

def blink(t):
	# while True:
	GPIO.setup(LedPin, GPIO.OUT)
	
	GPIO.output(LedPin, GPIO.HIGH)
	time.sleep(t)
	GPIO.output(LedPin, GPIO.LOW)
	time.sleep(t)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)
	GPIO.cleanup()

def RCtime (RCpin):
	# GPIO.setmode(GPIO.BCM)
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(RCpin, GPIO.IN)
	# This takes about 1 millisecond per loop cycle
	while (GPIO.input(RCpin) == GPIO.LOW):
		reading += 1
	return reading

if __name__ == '__main__':
	setup()
	# t = True
	while True:
		try:	
			[blink(0.5) for i in range(5)]
			[print(RCtime(18)) for i in range(50)]
			[blink(1) for i in range(4)]

		except KeyboardInterrupt:
			destroy()
