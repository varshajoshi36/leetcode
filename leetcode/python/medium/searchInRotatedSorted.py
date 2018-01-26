"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start + 1)/2)
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                if target > nums[end] and nums[end] >= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target < nums[start] and nums[start] <= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return -1

if __name__ == "__main__":
	sol = Solution()
	nums, target = [4, 5, 6, 7, 0, 1, 2], 2
	print sol.search(nums, target)
