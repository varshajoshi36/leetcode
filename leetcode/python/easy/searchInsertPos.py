'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end)/2
                if nums[mid] < target:
                    if mid == len(nums) - 1:
                        return len(nums)
                    elif nums[mid + 1] > target:
                        return mid + 1
                    else:
                        start = mid + 1
                elif nums[mid] > target:
                    if mid == 0:
                        return 0
                    elif nums[mid -1] < target:
                        return mid
                    else:
                        end = mid - 1

nums1, target1 = [1,3,5,6], 5
nums2, target2 = [1,3,5,6], 2 
nums3, target3 = [1,3,5,6], 7
nums4, target4 = [1,3,5,6], 0
nums5, target5 = [], 0

print searchInsert(nums1, target1)
print searchInsert(nums2, target2)
print searchInsert(nums3, target3)
print searchInsert(nums4, target4)
print searchInsert(nums5, target5)

