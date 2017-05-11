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
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	s_list = list(s)
	vowel_indices = [i for i in range(len(s)) if s[i] in vowels]
	
	i = 0
	j = len(vowel_indices) - 1
	while i < j:
		last_vowel = s[vowel_indices[j]]
		s_list[vowel_indices[j]] = s_list[vowel_indices[i]]
		s_list[vowel_indices[i]] = last_vowel
		i += 1
		j -= 1

	return "".join(s_list)

def main():
	print reverseVowels(raw_input())

if __name__ == '__main__':
	main()
