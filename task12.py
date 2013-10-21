#!/bin/env python

"""
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to 
fahrenheit, 
and f_to_c should do the opposite
"""
def c_to_f(some_number):
	first = float(some_number * 9)
	second = float(first/5)
	third = float(second + 32)
	print third

def f_to_c(some_number):
	first = float(some_number - 32)
	second = float(first * 5)
	third = float(second / 9)
	print third

f_to_c(50)
c_to_f(10)