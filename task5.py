#!/bin/env python

"""
Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""
s = "Hi there, my name is Slim"

def delete(s):
	beg_s = ''
	end_s = ''
	for i in range(6):
		beg_s += s[i]
	for i in range(12, len(s)):
		end_s += s[i]
		
	print beg_s + end_s

delete(s)