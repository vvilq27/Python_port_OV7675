import time
import serial
from serial import Serial
import os

import re
import numpy as np

from matplotlib import pyplot as plt

pic = []
t = []
d = {}
nums = list(range(240))

file = open('data.txt', 'w')

pic = [ ['00' for i in range(320)] for j in range(240)]
s = serial.Serial('COM8', 2000000)

c = 0

done = True

while done:
	l = s.readline()

	l = l.decode("UTF-8").rstrip('\r\n').split(',')

	tmp = l.copy()
	rowNum = 0

	if len(l) == 82:
		try:
			rowNum = int(l.pop())
		except Exception as e:
			print('error:\r\n{}\r\n{}'.format(e,l))
			continue

	del tmp[0]
	# print(rowNum)

	if rowNum in nums and len(tmp) == 81:
		nums.remove(rowNum)

		if len(nums) < 30:
			done = False

		if len(tmp) == 81:
			d[rowNum] = tmp

	numsLeft = ''
	for n in nums:
		numsLeft += str(n) + ','

	print(numsLeft)

# =========================
# DATA gathered
# =========================

# crete pic list & write data to file
for rowIdx in sorted(d):
	try:
		pic[rowIdx] = d[rowIdx]
	except:
		print('index out of index: {}'.format(rowIdx))

	line = ''

	for n in d[rowIdx]:
		line += str(n) + ','
	line += '\r\n'
	file.write(line)


file.close()
s.close()

# =========================
# make PIC
# =========================

for row in pic:
	
	# pop frame number if frame not "zero"
	if len(set(row)) != 1:
		row.pop()
	
	tmp = []

	for i in row:
	    for j in re.findall('..', i):
	            tmp.append(int(j, 16))
	    if len(tmp) > 319:
	    	break

	# fill missing data cells with '00'
	r = 320 - len(tmp)

	for i in range(r):
		tmp.append('00')

	# remove pixels if there is overhead
	if len(tmp) > 320:
		for i in range(len(tmp) - 320):
			tmp.pop()

	t.append(tmp)

plt.imshow(np.array(t, dtype='uint8'), interpolation='nearest', cmap='gray')	
plt.show()

