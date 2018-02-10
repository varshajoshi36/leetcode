"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)        
        start = 0
        end = length - 1
        while start < end and nums[start] == nums[end]:
            end -= 1
            
        while start <= end:
            length = (end - start + 1)
            if length <= 2:
                return min(nums[start], nums[end])
            if nums[start] < nums[end]:
                return nums[start]
            mid = start + (length/2)
            if nums[mid] >= nums[start]:
                start = mid
            else:
                end = mid
