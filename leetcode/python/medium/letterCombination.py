#! /usr/bin/python

"""Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below."""



def combineList(list1, list2):
	combined_list = []
	for item1 in list1:
		for item2 in list2:
			combined_list.append(item1 + item2)
	return combined_list



def letterCombinations(digits):
	num_letter = {'2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], 
			'5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], 
			'7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}
	length = len(digits)
	if length is 0:
		return []
	letter_list = num_letter[digits[0]]
	for i in range(1, length):
		letter_list = combineList(letter_list, num_letter[digits[i]])

	return letter_list

digits = ''
print letterCombinations(digits)
