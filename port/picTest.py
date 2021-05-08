import time
import serial
from serial import Serial
import os

import re
import numpy as np

from matplotlib import pyplot as plt
import threading


s = serial.Serial('COM6', 500000, timeout = 10)

ROW_CNT = 100
PIX_CNT = 100

data = []

pic = [ [0 for i in range(ROW_CNT)] for j in range(PIX_CNT)]

picReady = False


def getData():
	data = []
	rows = []

	rowCnt = 0
	line = ""
	brokenRows  = 0

	while True:
		# start = time.perf_counter()
		

		line = s.readline().hex()

		if line != "53544f500a" and rowCnt < ROW_CNT:
			if(len(line) != PIX_CNT*2):
					# print(str(rowCnt + 1) + ' ' + str(pixCnt))
				brokenRows += 1
				continue

			else:
				rowCnt += 1
				rows.append(line)

		# print(str(time.perf_counter() - start))

		else:
			print("finished collecting rows, broken rows: {}".format(brokenRows))
			s.readline()
			s.readline()
			s.readline()

			print('creating pic... '  + str(len(data)) + '\n')

			formatedLines = convertData(rows)

			try:
				draw(formatedLines)
			except:
				print("error generating img")

			formatedLines = []
			rows = []

			rowCnt = 0
			line = ""

			# while(True):
			# 	if(s.readline().hex() == "53544f500a"):
			# 		print("waiting...")
					
			# 		s.readline()
			# 		s.readline()
			# 		s.readline()
			# 		s.readline()
			# 		break

def convertData(rows):
	formatedLines = []

	remainingLines = [i for i in range(11, ROW_CNT+11)]
	for row in rows:
		formatedRow = [int(row[i:i+2], 16) for i in range(0, len(row), 2)]

		if formatedRow[0] not in remainingLines:
			continue

		try:
			remainingLines.remove(formatedRow[0])
		except:
			print('row {} out of range'.format(formatedRow[0]))

		formatedLines.insert(formatedRow[0], formatedRow)

	print(remainingLines)

	return formatedLines

def draw(picData):

	plt.imshow(np.array(picData, dtype='uint8'), interpolation='nearest', cmap='gray')	
	plt.ion()
	plt.show()

	plt.draw()
	plt.pause(0.001)


# x = threading.Thread(target=getData, args=())


# x.start()

getData()

