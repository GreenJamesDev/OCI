import RPi.GPIO as pins
import time

def Setup():
	# Initialize the pins.
	pins.setmode(pins.BOARD)

	pins.setup(12, pins.OUT)
	pins.setup(13, pins.OUT)
	pins.setup(15, pins.OUT)
	pins.setup(16, pins.OUT)
	pins.setup(18, pins.OUT)

	# Set active low pins to high.
	pins.output(13, 0)
	pins.output(18, 1)

# Shift register pin variables.
data = 12
outputE = 13
latch = 15
clock = 16
clear = 18

# Display shift register contents.
def DisplayData():
	pins.output(latch, 1)
	time.sleep(0.1)
	pins.output(latch, 0)

def PulseLatch():
	pins.output(latch, 1)
	time.sleep(0.5)
	pins.output(latch, 0)

def InputData(indata):
	pins.output(data, indata)
	pins.output(clock, 1)
	time.sleep(0.1)
	pins.output(clock, 0)
	pins.output(data, 0)

def ClearDisplay():
	pins.output(clear, 1)
	time.sleep(0.1)
	pins.output(clear, 0)
	DisplayData()

# Decode and display a binary sequence from a string.
def SendByte(s):
	print("Outputting " + s + " to the display.")
	for ch in s:
		InputData(int(ch))
	DisplayData()

# NUMBERS
def Seven():
	SendByte("10011000")

def One():
	SendByte("10010000")

def Two():
	SendByte("01111010")

def Three():
	SendByte("11011010")

def Four():
	SendByte("10010110")

def Five():
	SendByte("11001110")

def Six():
	SendByte("11101110")

def Eight():
	SendByte("11111110")

def Nine():
	SendByte("10011110")

def Zero():
	SendByte("11111100")

def DecimaL():
	SendByte("00000001")





