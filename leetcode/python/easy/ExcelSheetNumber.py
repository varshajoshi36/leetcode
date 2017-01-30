'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
import string

def titleToNumber(s):
        """
        :type s: str
        :rtype: int
        """
	alphabets = list(string.ascii_uppercase)
	multiplier = 1
	number = 0
	for i in range(len(s) - 1, -1, -1):
		number += multiplier * (alphabets.index(s[i]) + 1)
		multiplier *= 26

	return number

s = 'Z'
print titleToNumber(s)
	
