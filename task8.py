#!/bin/env python

"""
Given two dictionaries, d1 and d2, update the contents of d1 with the contents of d2, overwriting any existing keys
eg:
    d1 = {"a":1, "b":2}
    d2 = {"a":3, "c":4}

    becomes

    d1 = {"a":3, "b":2, "c":4}
"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

def change_dict(d1, d2):
	for i in range(len(d2)):
		for key in d2:
			for keys in range(len(d1)):
				if not key in d1:
					d1[key] = d2[key]
				elif d1[key] != d2[key]:
					d1[key] = d2[key]
	print d1


change_dict(d1, d2)
