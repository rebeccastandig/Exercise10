#!/bin/env python

"""
Given two dictionaries, d1 and d2, merge the contents of d1 with the contents of d2, adding to the values of existing keys
eg:
    d1 = {"a": 1, "b":2}
    d2 = {"a": 3, "d": 4}

    becomes

    d1 = {"a": 4, "b":2, "d":4}

"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

def add_dict(d1, d2):
	d2_keys = d2.keys()
	d1_keys = d1.keys()
	# print "d1: ", d1_keys
	# print "d2: ", d2_keys
	for key in d2_keys:
		if key not in d1_keys:
			d1[key] = d2[key]
		else:
			d1[key] = d2[key] + d1[key]
	print d1


add_dict(d1, d2)