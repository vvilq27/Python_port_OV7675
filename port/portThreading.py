import time
import serial
import os
# import multiprocessing
import threading
from queue import Queue


# while True:

# file = open("data.txt", "wb")
s = serial.Serial('COM6', 500000)

PIXSPERROW = 250

t = list()
badRowsCnt = 0
missedRowIndexes = [i for i in range(11,163)]

line = 'hello'


def readPort(name):
	line = s.readline().hex()

	print('{} {}'.format(name, len(line)))

def printLine(name):
	global line

	while(True):
		# print(len(line))
		if len(line) != 0:
			print(line[:40])
			line = ''

lastTime = time.time()
frameLength = 0

while(True):
	if s.in_waiting > 0:
		data = s.read(s.in_waiting).hex()
		print(len(data))
		frameLength += len(data)

		currentTime = time.time()

		if currentTime - lastTime > 0.9:
			print('fram grabbed of size: {}'.format(frameLength))
			frameLength = 0
			lastTime = currentTime


'''
readThread = multiprocessing.Process(target=readPort, args=(1,))
printThread = multiprocessing.Process(target=printLine, args=(2,))

readThread.start()
'''

# 
# printThread.start()
# readThread.join()
# printThread.join()




# def threader():
# 	while(True):
# 		readPort(1)




# q = Queue()

# readThread = threading.Thread(target=threader)
# readThread.deamon = True

# readThread.start()

# printThread = threading.Thread(target=printLine, args=(2,))
# printThread.deamon = True

# printThread.start()


# for worker in range(20):
# 	q.put(worker)

# q.join()







'''
while True:

	l = s.readline().hex()

	if len(l) == PIXSPERROW*2 and l != "53544f500a":
		# pixelCnt = int(l[-4:-2], 16)

		rowIndex = int(l[:2], 16)
		# print("g: {}".format(str(rowIndex)))
		try:
			missedRowIndexes.remove(rowIndex)
		except:
			print("bad row: {} ".format(str(rowIndex)))

	else:
		badRowsCnt += 1
		print(l)
		# print(str(int(l[:2],16)) + " " + str(int(l[-4:-2],16)) + ' ' + str(len(l)))

	if l == "53544f500a":
		s.readline()
		s.readline()

		print("FRAME CPLT, bad rows : {}".format( badRowsCnt))	
		print(missedRowIndexes)
		missedRowIndexes = [i for i in range(11,163)]
		badRowsCnt = 0

'''

'''
	if len(l) > 100:
	# row num | pixl cnt | pic len
		print(str(int(l[:2], 16)) + ' ' + str(int(l[-4:-2], 16)) + ' '  + str(len(l)) + ' ' + str(l[380:]) )
	elif l == "53544f500a":
		print("FRAME CPLT")

'''

	# print('\n')
	# if int(l.decode("UTF-8").rstrip('\r\n').split(',').pop()) < 10:
	# 	break

# while True:
# 	pass
# while True:
# 	l = s.readline()
# 	if int(l.decode("UTF-8").rstrip('\r\n').split(',').pop()) > 238:
# 		break
# 	t.append(l)
# 	# file.write(l)



	# if b"hscnt" in l:
	# 	break
# print(len(t))
# for line in t:
# 	file.write(line)

# file.close()
# s.close()

# # print(t[len(t)-1])

# print("img")
# os.system("imageMakerFile.py 1")

