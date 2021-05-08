import serial
from serial import Serial

pic = []
d = {}
nums = list(range(240))

pic = [ ['00' for i in range(320)] for j in range(240)]
s = serial.Serial('COM8', 2000000)

c = 0

done = True

while done:
	l = s.readline()

	l = l.decode("UTF-8").rstrip('\r\n').split(',')
	# print(row)
	tmp = l.copy()

	rowNum = int(l.pop())

	if int(rowNum) in nums:
		nums.remove(rowNum)

	if len(nums) < 50:
		done = False

	d[rowNum] = tmp

s.close()


for rowIdx in sorted(d):
	pic[rowIdx] = d[rowIdx]


for row in pic:
	if len(row) != 82:
		print(row)
