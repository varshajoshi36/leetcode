'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

def search(nums, target):
	length = len(nums)
	start = 0
	end  = length - 1

	while start < end:
		mid =  (start + end)/2
		if nums[mid] > nums[end]:
			start = mid + 1
		else:
			end = mid

	rot = start
	start = 0
	end = length - 1
	while start <= end:
		mid = (start + end) / 2
		real_mid = (mid + rot) % length
		if nums[real_mid] == target:
			return real_mid
		if nums[real_mid] < target:
			start = mid + 1
		else:
			end = mid - 1
	


nums = [5, 6, 7, 8, 9, 3, 4]
print search(nums, 3)
