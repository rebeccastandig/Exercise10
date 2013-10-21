#!/bin/env python

"""
Given the string s, produce a list composed of all the single characters from the original string
eg:
    s = "Hello"
    becomes
    l = {"H", "e", "l", "l", "o"}
"""
s = "Hi there, my name is Slim"

def split_s(s):
	l = []
	for i in s:
		l.append(i)
	print l

	# this way also works:
	# l = []
	# for letter in s:
	# 	l += letter
	# print l

split_s(s)
