#! /usr/bin/python

"""if a string is permutation of other"""

def is_permutation(s1, s2):
	if len(s1) is not len(s2):
		return False
	for ch in s1:
		if s1.count(ch) is not s2.count(ch):
			return False
	return True


s1, s2 = 'abc', 'cbaa'
print s1, s2
print is_permutation(s1, s2)
			
		
