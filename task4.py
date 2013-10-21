#!/bin/env python

"""
Given the string s, split it into two strings, s2 and s3, 
s2 containing the first 5 letters of the string, 
and s3 containing the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""
s = "Hi there, my name is Slim"

def split_strings(s):
	# s2 = s[:5]
	# s3 = s[5:]
	# print "s2: ", s2
	# print "s3: ", s3

	s2 = ""
	s3 = ""
	for i in range(5):
		s2 += s[i]
	for i in range(5,len(s)):
		s3 += s[i]
	print s2
	print s3


split_strings(s)
