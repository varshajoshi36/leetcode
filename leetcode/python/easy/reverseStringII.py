"""

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

def reverseWords(s):
	s_list = s.split()
	reversed_str = []
	for string in s_list:
		reversed_str.append( string[::-1])

	return " ".join(reversed_str)

def main():
	print reverseWords(raw_input())

if __name__ == '__main__':
	main()
