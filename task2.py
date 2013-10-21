#!/bin/env python
"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""
d = {"q": 5, "m": 3, "z":2, "a": 10}

def bubblesort(l):
	unordered = True
	while unordered == True:
		unordered = False
		for i in range(len(l)-1):
			if l[i] < l[i+1]:
				temp = l[i]
				l[i] = l[i+1]
				l[i+1] = temp
				unordered = True
	return l

def printdict(d):
	sortedkeys = bubblesort(d.keys())
	sortedkeys.reverse()
	for key in sortedkeys:
		value = d[key]
		print key,",",value




printdict(d)