'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
    Given input array nums = [3,2,2,3], val = 3

    Your function should return length = 2, with the first two elements of nums being 2.
'''

def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    end = len(nums) - 1
    while nums[end] == val and end >= 0:
        end -= 1
    for i in range(len(nums)):
        if i > end:
            break
        if nums[i] == val:
            nums[i] = nums[end]
            if end > 0:
                end -= 1
            while nums[end] == val and end >= 0:
                end -= 1

    print end, nums
    return end + 1


nums, val = [0,4,4,0,4,4,4,0,2], 4
print removeElement(nums, val)
