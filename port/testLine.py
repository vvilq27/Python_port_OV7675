import serial
from serial import Serial
from collections import Counter

s = serial.Serial('COM8', 2000000)

while b'hscnt' not in s.readline():
	pass



print(s.readline().decode("UTF-8").rstrip('\r\n').split(',').pop())

while int(s.readline().decode("UTF-8").rstrip('\r\n').split(',').pop()) < 235:
	pass

a = s.readline()

t = a.decode("UTF-8").rstrip('\r\n').split(',')
# t.pop()


print(t)
# print(Counter(t))
print(len(t))