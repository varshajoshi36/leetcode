'''
A magic index in an array A [ 0 . . .n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
'''

def magic_index(nums):
	first = 0
	last = len(nums) - 1
	while first <= last:
		mid = first + (last - first)/2
		if nums[mid] is mid:
			return mid
		elif nums[mid] < mid:
			first = mid + 1
		else:
			last = mid -1
	return -1


nums = [int(ele) for ele in raw_input().split()]
print magic_index(nums)

