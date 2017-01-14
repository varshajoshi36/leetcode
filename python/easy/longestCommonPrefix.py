#! /usr/bin/python
import sys


#Write a function to find the longest common prefix string amongst an array of strings.
#working solution

def longestCommonPrefix(strs):
	common_prefix = ""	
	num_strings = len(strs)
	if num_strings == 0:
		return common_prefix
	shortest_len = len(min(strs, key = len)) 
	
	for i in range(shortest_len):
		j = 1
		while j < num_strings and strs[0][i] is strs[j][i]:
			print "in while j:", j
			j += 1
		if j == num_strings:
			common_prefix += strs[0][i]
		else:
			break
	
	return common_prefix


strs = ["aca", "acba"]
print longestCommonPrefix(strs)
				
