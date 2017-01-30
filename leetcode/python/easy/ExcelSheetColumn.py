'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

import string


def convertToTitle(n):
        """
        :type n: int
        :rtype: str
        """
	alphabets = list(string.ascii_uppercase)
	column = ''
	while n > 0:
		mod = n % 26
		column = alphabets[mod - 1] + column
		if mod is 0:
			n = n/26 - 1
		else:
			n = n/26
	return column

n = 1000 
print convertToTitle(n)
