'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr(self, haystack, needle):
	if needle not in haystack:
		return -1
	return haystack.index(needle)
