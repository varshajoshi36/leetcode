"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""

def isIsomorphic(s, t):
	if len(set(s)) != len(set(t)):
		return False

	letter_map = {}
	for i in range(len(s)):
		if s[i] not in letter_map.keys():
			letter_map[s[i]] = t[i]
		else:
			if t[i] != letter_map[s[i]]:
				return False

	return True


def main():
	str1, str2 = raw_input().split(',')
	print isIsomorphic(str1.strip(), str2.strip())

if __name__ == '__main__':
	main()
