#! /usr/bin/python
import sys
def threeSumClosest(nums, target):
	diff = sys.maxint
	for i in range(0, len(nums) - 2):
		for j in range(i+1, len(nums)-1):
			for k in range (j+1, len(nums)):
				if abs(target - (nums[i] + nums[j] + nums[k])) < diff:
					diff = abs(target - (nums[i] + nums[j] + nums[k]))
					sum1 = nums[i] + nums[j] + nums[k]
					if diff is 0:
						return target

	return sum1


target, nums = 1, [1,2,3,45,0,-1]
print target, nums
print threeSumClosest(nums, target)
