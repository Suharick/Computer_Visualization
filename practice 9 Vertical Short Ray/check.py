from math import *
H = []
# INSERT ANSWER HERE (function GetZ())
def GetZ(x, y):
	return 10

def strR(r):
    return '{0:.2f}'.format(r)
f = open('H.txt', 'r')
wH = int(f.readline())
hH = int(f.readline())
for x in range(wH):  
	H.append([])
	for y in range(hH):
		z = float(f.readline())
		H[x].append(z)
f.close()

x, y = map(float, input().split())
print(strR(GetZ(x, y)))
