'''Bubble sort'''

import sys


def bubblesort(mydata):
	for row in range(len(mydata)-1):
		for i in range(len(mydata)-1-row):
			if(mydata[i] > mydata[i+1]):
				temp = mydata[i]
				mydata[i] = mydata[i+1]
				mydata[i+1] = temp







f = open(sys.argv[1])


'''read the contents of file in the list...'''
fline = f.readlines()
'''as our file contains only a single line we can directly put the numbers in
 a single dimensional array....'''
mydata = [int(val) for val in fline[0].split()]

bubblesort(mydata)
print('sorted array:', mydata)
