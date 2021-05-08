import time
import serial
import os



# while True:

# file = open("data.txt", "wb")
s = serial.Serial('COM6', 512000)

PIXSPERROW = 250

t = list()
badRowsCnt = 0
missedRowIndexes = [i for i in range(11,163)]


while True:

	l = s.readline().hex()

	if len(l) == PIXSPERROW*2 and l != "53544f500a":
		# pixelCnt = int(l[-4:-2], 16)

		rowIndex = int(l[:2], 16)
		# print("g: {}".format(str(rowIndex)))
		try:
			missedRowIndexes.remove(rowIndex)
		except:
			print("bad row: {} len: {}".format(str(rowIndex), str(len(l))))

	else:
		badRowsCnt += 1
		# print(l)
		# print(str(int(l[:2],16)) + " " + str(int(l[-4:-2],16)) + ' ' + str(len(l)))

	if l == "53544f500a":
		s.readline()
		s.readline()

		print("FRAME CPLT, bad rows : {}".format( badRowsCnt))	
		print(missedRowIndexes)
		missedRowIndexes = [i for i in range(11,163)]
		badRowsCnt = 0


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

