#!/bin/env python

s = """
Given a multiline string 's', 
print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""
s = "Sorry,\nMy people need me\nI must go"
def print_lines(s):
	counter = 0
	split_on_lines = s.split("\n")
	for i in range(len(split_on_lines)):
		counter += 1
		print counter, ".", split_on_lines[i]

print_lines(s)