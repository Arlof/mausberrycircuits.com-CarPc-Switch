    # Import the RPi.GPIO and OS
import RPi.GPIO as GPIO
import os
import time

    # GPIO port setup
GPIO.setmode(GPIO.BOARD) # Set pin numbering to BOARD numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set up pin 16 (23) as an input, pulled down
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 1) # Set pin 18 (24) value to 1

## 
##	Functions
##

def hold_on():
    print("In Holding Pattern\n\r")
    GPIO.wait_for_edge(16, GPIO.RISING)
    trig_event()

def hold_shutdown():
    print("Cancelled Shutdown\n\r")
    GPIO.wait_for_edge(16, GPIO.FALLING)

def trig_event():
    print("Interrupt Triggered\n\r")
    time.sleep(5)
    if (GPIO.input(16) == 1):
	print("Pin High")	## 0  V Switched Present
	print("Shutting Down")	
	os.system('poweroff')	## Shut Down System
    if (GPIO.input(16) == 0):
	print("Pin Low")	## 12 V Switched Present
	print("Going Back To Hold")
	hold_on()

hold_on()

print("Loop Broke")


