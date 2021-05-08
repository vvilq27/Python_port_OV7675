from PIL import Image
import numpy as np

a = list()

with open('data.txt') as f:
     for line in f.readlines():
             a.append(line.rstrip('\n').split(','))


a.pop()
a.pop()

for line in a:
	line.pop()
	for i, j in enumerate(line):
		line[i] = bytes([int(j)])


print('sizes: ')
print(len(a))
print(len(a[4]))


# mode L is for 8bit gray scale
img = Image.frombytes(mode='L', size =tuple([len(a[4]),len(a)]), data= np.array(a))


img.save('test.png')


