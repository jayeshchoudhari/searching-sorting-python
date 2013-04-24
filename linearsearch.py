'''This program is for linear search in python.
The complexity is O(n)...
It takes the input from the file which contains
numbers separated by space'''

'''Run the program as python3.2 linearsearch.py inputfile.txt'''

import sys 
'''to read the command line arguments'''

def linearsearch(mydata, search_element):
	for i in range(len(mydata)):
		if(search_element == mydata[i]):
			return i
	return -1

f = open(sys.argv[1])


'''read the contents of file in the list...'''
fline = f.readlines()
'''as our file contains only a single line we can directly put the numbers in
 a single dimensional array....'''
mydata = [int(val) for val in fline[0].split()]

'''Get the input from the user---the element to be searched...'''
search_element = input('Enter the value - ')
search_element = int(search_element)
'''typecast required as the value is read as string...'''
'''for more information of the type of value read use the statement commented below'''
'''print(type(search_element))'''
'''call to function linearsearch()'''
returned_value = linearsearch(mydata, search_element)


if(returned_value == -1):
	print('value not found...')
else:
	print('value found at :', returned_value+1, 'position ')
