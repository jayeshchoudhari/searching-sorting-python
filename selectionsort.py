'''Selection sort'''

import sys


def selectionsort(mydata):
	for targetidx in range(len(mydata) - 1):
		minidx = targetidx
		minval = mydata[minidx]
		for i in range(targetidx + 1, len(mydata)):
			value = mydata[i]
			if(value < minval):
				minidx = i
				minval = value
		#swap the values at targetidx and miniidx
		mydata[minidx] = mydata[targetidx] 
		mydata[targetidx] = minval






f = open(sys.argv[1])


#'''read the contents of file in the list...'''
fline = f.readlines()
'''as our file contains only a single line we can directly put the numbers in
 a single dimensional array....'''
mydata = [int(val) for val in fline[0].split()]

selectionsort(mydata)
print('sorted array:', mydata)
