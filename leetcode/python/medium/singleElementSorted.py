"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
"""
def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    length = len(nums)
    start = 0
    end = len(nums) - 1
    while start < end:
        size = end - start + 1
        mid = start + (size / 2)
        if size == 3:
            if nums[mid] == nums[mid - 1]:
                return nums[mid + 1]
            else:
                return nums[mid - 1] 
        if nums[mid] == nums[mid + 1]:
            if (end - mid + 1) % 2 != 0:
                start = mid
            else:
                end = mid - 1
        elif nums[mid] == nums[mid - 1]:
            if (mid - start + 1) % 2 != 0:
                end = mid
            else:
                start = mid + 1
        else:
            return nums[mid]

nums = [0,1,1,2,2,5,5]
print singleNonDuplicate(nums)
