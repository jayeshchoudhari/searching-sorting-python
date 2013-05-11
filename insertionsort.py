'''Insertion sort'''

import sys


def insertionsort(mydata):
	for row in range(1, len(mydata)):
		for i in range(row, 0, -1):
			if(mydata[i] < mydata[i-1]):
				temp = mydata[i]
				mydata[i] = mydata[i-1]
				mydata[i-1] = temp







f = open(sys.argv[1])


'''read the contents of file in the list...'''
fline = f.readlines()
'''as our file contains only a single line we can directly put the numbers in
 a single dimensional array....'''
mydata = [int(val) for val in fline[0].split()]
		
insertionsort(mydata)
print('sorted array:', mydata)
