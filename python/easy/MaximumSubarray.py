#! /usr/bin/python

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):
	if len(nums) < 1:
		return 0
	maxSoFar = nums[0]
	maxHere = nums[0]
	for element in nums:
		maxHere = max(maxHere + element, element)
		maxSoFar = max(maxSoFar, maxHere)

	return maxSoFar

nums = [-2,1,-3,4,-1,2,1,-5,4]
print maxSubArray(nums)
