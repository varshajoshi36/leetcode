#! /usr/bin/python
import re

"""Write a method to replace all spaces in a string with'%20'. You may assume that
the string has sufficient space at the end of the string to hold the additional
characters, and that you are given the "true" length of the string. (Note: if imple-
menting in Java, please use a character array so that you can perform this opera-
tion in place.)"""

def replace_white_spaces(s):
	return re.sub(r"\s", '%20', s)


s = "I am a disco dancer"
print s
print replace_white_spaces(s)
