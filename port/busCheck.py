import time
import serial
from serial import Serial
import os

import re
import numpy as np

from matplotlib import pyplot as plt

a = list()
t = []
pic = [ ['00' for i in range(320)] for j in range(240)]
s = serial.Serial('COM8', 2000000)


while b"\r\n" not in s.readline():
	pass

c = 0

while True:
	l = s.readline()

	y = l.decode("UTF-8").rstrip('\r\n').split(',')

	c += 1
	if c > 239:
		break

	a.append(l.decode("UTF-8").rstrip('\r\n').split(','))

# for row in a:
# 	print(row)

for row in a:
	pic[int(row[-1])] = row;

s.close()

# DATA gathered, make PIC

for row in pic:
	
	# pop frame number if frame not "zero"
	if len(set(row)) != 1:
		row.pop()
	# else:
	
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

	if len(tmp) > 320:
		# print(tmp)
		# print(len(tmp))

		for i in range(len(tmp) - 320):
			tmp.pop()

	t.append(tmp)

# print(len(t))
# for row in t:
# 	print(len(row))




# tab = [[0 for i in range(320)] for j in range(240)]

# print(len(pic))
# print(len(pic[0]))

# for i in range(240):
# 	for j in range(320):
# 		try:
# 			tab[i][j] = int(t[i][j])
# 		except (IndexError, ValueError) as e:
# 			print('ero {}, {}'.format(i,j))

plt.imshow(np.array(t, dtype='uint8'), interpolation='nearest', cmap='gray')
plt.show()



# img = Image.frombytes(mode='L', size =tuple([50,50]), data= np.array(tab))


# img.save('test.png')

# file = open("data.txt", "w")

# for line in pic:
# 	lineInt = ''
# 	for i in line:
# 		lineInt += '{},'.format(str(i))

# 	# print(lineInt)
# 	file.write(lineInt)


# print(pic[0])

# for row in pic:
# 	for i in row:
# 		if i == '':
# 			print('hey')
# 			continue
# 		i = bytes(int(i))

# # print(pic[0])

	# k = s.readline().decode("UTF-8").rstrip('\r\n').split(',')[-1]

	# if int(k) == 100:
	# 	print(k)

# mode L is for 8bit gray scale
