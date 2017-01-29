#! /usr/bin/python

"""determine if a string has all unique characters. Additional data structure is not available"""

def is_unique(s):
	is_unique = True
	for i in range(len(s)):
		if s[i] in s[i+1:]:
			is_unique = False
			break

	return is_unique

s = 'abcde'
print s
print is_unique(s)

