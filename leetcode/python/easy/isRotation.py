#! /usr/bin/python

"""Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, si and s2, write code to check if s2 is
a rotation of si using only one call to isSubstring (e.g.,"waterbottle"is a rota-
tion of "erbottlewat")."""

def is_substring(s1, s2):
	if s1 in s2:
		return True
	else:
		return False

def is_rotation(s1, s2):
	if len(s1) is len(s2):
		starting_index = s1.index(s2[0])
		s2s2 = s2 + s2
		if is_substring(s1, s2s2):
			return True
	else:	
		return False


s1, s2 = 'waterbottlew', 'bottlewwater'
print s1, s2
print is_rotation(s2, s1)
