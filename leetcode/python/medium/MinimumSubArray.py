
#! /usr/bin/python
import sys

def MinimumSum(s, nums):
	i, j, loc_sum, min_len = 0, 0, 0, sys.maxint
	while j < len(nums):
		while (j < len(nums) and loc_sum < s):
			loc_sum += nums[j]
			j += 1
		if(loc_sum >= s):
			while (loc_sum >= s and i < j):
				loc_sum -= nums[i]
				i += 1
			min_len = min(min_len, j - i + 1)
	if loc_sum == sys.maxint:
		return 0
	return min_len

s, nums = 7, [2,3,1,2,4,3]
print MinimumSum(s, nums)


