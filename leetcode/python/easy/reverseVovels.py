"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

def reverseVowels(s):
	vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	s_list = list(s)
	last_vovel_index = max([s.rfind(x) for x in vovels])
	
	i = 0
	while i < last_vovel_index and i < len(s):
		if s_list[i] in vovels:
			last_vovel = s[last_vovel_index]
			s_list[last_vovel_index] = s_list[i]
			s_list[i] = last_vovel
			last_vovel_index = max([s[:last_vovel_index].rfind(x) for x in vovels])
		i += 1
			
			
	return "".join(s_list)

def main():
	print reverseVowels(raw_input())

if __name__ == '__main__':
	main()
