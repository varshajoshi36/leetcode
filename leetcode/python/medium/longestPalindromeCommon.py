#! /usr/bin/python

def longestPalindrome(s):
	r_s = s[::-1]
	print r_s
	answer = ""
	palindrome = ""
	len1 = len(s)
	for i in range(len1):
		match = ""
		for j in range(len1):
			if i + j < len1 and s[i + j] is r_s[j]:
				match += r_s[j]
				if i + j == len1 - 1:
					if (len(match) > len(answer)): 
						print "match", match
						answer = match
					match = ""
			else:
				if (len(match) > len(answer)): 
					print "match", match
					answer = match
				match = ""
			print "answer", answer
	if r_s.index(answer) == len1 - s.index(answer) - len(answer):
		palindrome = answer
	return palindrome


s = "abbadfg"
print longestPalindrome(s)
					
