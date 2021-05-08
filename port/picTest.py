import time
import serial
from serial import Serial
import os

import re
import numpy as np

from matplotlib import pyplot as plt
import threading


s = serial.Serial('COM6', 512000, timeout = 10)

ROW_CNT = 150
PIX_CNT = 250

data = []

pic = [ [0 for i in range(ROW_CNT)] for j in range(PIX_CNT)]

picReady = False


def getData():
	data = []

	rowCnt = 0
	line = ""

	while True:
		# start = time.perf_counter()
		

		line = s.readline().hex()

		if line != "53544f500a":

			# split string into hex bytes and translate them into integers, then put in array
			rowPixs = [int(line[i:i+2], 16) for i in range(0, len(line), 2)]
			pixCnt = len(rowPixs)

			# print("pxcnt: {}".format(pixCnt))

			if(pixCnt != PIX_CNT):
					print(str(rowCnt + 1) + ' ' + str(pixCnt))

			else:
				rowCnt += 1

				data.insert(rowPixs[0], rowPixs)

		# print(str(time.perf_counter() - start))

		else:
			print("finished collecting rows: {}".format(rowCnt))
			s.readline()
			s.readline()
			s.readline()

			print('creating pic... '  + str(len(data)) + '\n')

			try:
				draw(data)
			except:
				print("error generating img")

			data = []

			rowCnt = 0
			line = ""

		# while(True):
		# 	if(s.readline().hex() == "53544f500a"):
		# 		print("waiting...")
		# 		s.readline()
		# 		s.readline()
		# 		s.readline()
		# 		break


def draw(picData):

	plt.imshow(np.array(picData, dtype='uint8'), interpolation='nearest', cmap='gray')	
	plt.ion()
	plt.show()

	plt.draw()
	plt.pause(0.001)


# x = threading.Thread(target=getData, args=())


# x.start()

getData()

