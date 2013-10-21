#!/bin/env python

"""
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""
l = [(1,2), (3,1), (17, 35), (81,20)]

def sort_by_tuples(l):
	unordered = True
	while unordered == True:
		unordered = False
		for i in range(len(l)-1):
			if l[i][1] > l[i+1][1]:
				temp = l[i]
				l[i] = l[i+1]
				l[i+1] = temp
				unordered = True
	print l
sort_by_tuples(l)