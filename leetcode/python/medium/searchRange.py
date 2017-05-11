"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]
"""

def searchRange(nums, target):
	start = 0
	end = len(nums) - 1

	if target < nums[0] or target > nums[-1] or len(nums) == 0:
		return [-1, -1]

	range_start = start
	range_end = end

	while start < end - 1:
		mid = (start + end)/2
		if nums[mid] < target:
			range_start = mid
			start = mid
		else:
			if range_start < range_end - 1:
				if nums[mid - 1] >= target:
					range_end = mid - 1
				else:
					range_end = mid
			end = mid - 1

	return [range_start, range_end]

def main():
	nums = map(int, raw_input().split(','))
	target = int(raw_input())
	print searchRange(nums, target)

if __name__ == "__main__":
    main()
