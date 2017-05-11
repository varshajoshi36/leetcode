"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""

def reverseStr(s, k):
	s_list = list(s)
	for i in range(0, len(s), 2*k):
		reversedList = s_list[i : i + k][-1 : -(k+1) : -1]
		s_list[i : i + k] = reversedList

	return "".join(s_list)

def main():
	print reverseStr(raw_input(), int(raw_input()))

if __name__ == '__main__':
	main()
