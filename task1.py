#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]

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

print bubblesort(l)