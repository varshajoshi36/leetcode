#! /usr/bin/python

def MergeLexicographical(s1, s2):
	length1, length2 = len(s1), len(s2)
	i,j = 0, 0
	r_s = ''
	while (i < length1 and j < length2):
		if s1[i] <= s2[j]:
			r_s += s1[i]
			i += 1
		else:
			r_s += s2[j]
			j += 1

	while i < length1:
		r_s += s1[i]
		i += 1
	
	while j < length2:
		r_s += s2[j]
		j += 1

	return r_s


s1, s2 = 'abad', 'bbde'
print MergeLexicographical(s1, s2)

