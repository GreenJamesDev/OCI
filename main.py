 # IMPORTS --------------
import RPi.GPIO as pins
import sys
import time
import subprocess as sproc
import os
import urllib2
import socket
from display import DecimaL
from display import Zero
from display import One
from display import Setup
# ----------------------


# Setup the GPIO pins for the program.
def pin_init():
	STATUS_LED = 11

	pins.setmode(pins.BOARD)
	pins.setup(7,pins.OUT)
	pins.setup(11,pins.OUT)
	pins.setup(12,pins.IN,pull_up_down=pins.PUD_DOWN)
	Setup()

# ==== UNUSED ======================================================
# When an error occurs, make the red LED blink as many times as
# the error code specifies, then keep the red LED on forever.
def error(err_code):
	print('The system has halted with error code:', err_code)
	for i in range(err_code):
		pins.output(7,pins.LOW)
		time.sleep(1)
		pins.output(7,pins.HIGH)
		time.sleep(1)
# ==================================================================

# Make the yellow status LED blink.
def status_blink():
	pins.output(11,pins.HIGH)
	time.sleep(0.3)
	pins.output(11,pins.LOW)
	time.sleep(0.3)

# Test the internet connection before loading the rest of the
# program. If the test fails, the red error LED blinks, then the
# application closes.
def test_net():
	status = 0

	try:
		status_blink()
    		urllib2.urlopen("https://google.com", timeout=10)
	except urllib2.URLError as err:
    		status = 1

	if status == 0:
		print('Ready...')
		DecimaL()
	else:
		print("Not Connected")
		One()

# Set status LEDs to low then restart the system.
def exit():
	pins.output(11,pins.LOW)
	pins.output(7,pins.LOW)
	sproc.call("sudo poweroff", shell=True)

def flush():
	pins.output(11,pins.LOW)
	Zero()

# Main code calls.

pin_init() # Setup the pins.
Zero()
time.sleep(10)
test_net() # Test the connection.


