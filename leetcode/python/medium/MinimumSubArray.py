#! /usr/bin/python

def MinimumSum(s, nums):
	min_no = len(nums)
	index = 0
	while index < len(nums):
		loc_min = nums[index]
		loc_count = 1
		loc_ind = index + 1
		while loc_min < s and loc_count < min_no and loc_ind < len(nums):
			loc_min += nums[loc_ind]
			loc_ind += 1
			loc_count += 1
			
		if loc_count < min_no and loc_min >= s:
			min_no = loc_count
		index += 1

	return min_no

s, nums = 7, [2,3,1,2,4,3]
print MinimumSum(s, nums)


