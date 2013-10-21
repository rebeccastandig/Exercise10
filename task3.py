#!/bin/env python

"""
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 10]
l2 = [93, 2, 23, 77, 66]

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

def intersection(l1, l2):
	l3 = []
	for number in range(len(l1)):
		for another_number in range(len(l2)):
			if l1[number] == l2[another_number]:
				if l1[number] not in l3:
					l3.append(l1[number])
			if l1[number] not in l3:
				l3.append(l1[number])
			if l2[another_number] not in l3:
				l3.append(l2[another_number])
	sorted_l3 = bubblesort(l3)
	sorted_l3.reverse()
	print sorted_l3

intersection(l1, l2)

