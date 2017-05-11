"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""
import re

def lengthOfLastWord(s):
	s = re.sub(r'([^\s\w]|_|\d+)+', '', s)
	return len(s.strip().split(' ')[-1])

def main():
	print lengthOfLastWord(raw_input())

if __name__ == "__main__":
	main()
