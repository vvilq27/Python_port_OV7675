import serial
from serial import Serial
import os
from time import sleep


# while True:

# file = open("data.txt", "wb")
s = serial.Serial('COM4', 115200, timeout=0.2)

while True:
	print(s.read(3))
