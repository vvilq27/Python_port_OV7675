import matplotlib.pyplot as plt
import numpy as np

al = [line.rstrip('\n') for line in open('data.txt')]
ar = [s.split(',') for s in al]

ar.pop()
ar.pop()

print(len(ar))

for l in ar:
	l.pop()

a = np.array(ar, dtype="float")


plt.imshow(a, interpolation='nearest', cmap="gray")
plt.show()