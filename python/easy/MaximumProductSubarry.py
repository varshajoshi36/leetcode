#! /usr/bin/python

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

def maxProduct(nums):
	if len(nums) < 1:
		return 0
	maxSoFar = nums[0]
	local_max, local_min = nums[0], nums[0]
	for element in nums[1:]:
		if element < 0:
			local_max, local_min = local_min, local_max
		local_max = max(local_max * element, element)
		local_min = min(local_min * element, element)
		maxSoFar = max(maxSoFar, local_max)

	return maxSoFar

nums = [-2,1,-3,4,-1,2,1,-5,4]
print maxProduct(nums)
