'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''


def reverseWords(s):
	return_s = ''
	s = s.lstrip()
	while(len(s) > 0):
		if ' ' in s:
			white_space_index = s.index(' ')
		else:
			white_space_index = len(s)
		return_s = s[:white_space_index] + ' ' + return_s
		s = s[white_space_index:]
		s = s.lstrip()

	return return_s.rstrip()


s = ''
print reverseWords(s)
