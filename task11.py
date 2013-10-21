#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""

def title(my_title):
	my_t_split = my_title.split()
	new_title = ''
	no_caps = ["a", "the", "to", "at", "in", "of", "with", "and", "but", "or"]
	for char in my_t_split:
		if char == my_t_split[0]:
			upper = char[0].upper()
			word = upper + char[1:]
		elif char not in no_caps:
			upper = char[0].upper()
			word = upper + char[1:]
		else:
			word = char
		new_title += word + " "
	print new_title

title("a tale of two cities")