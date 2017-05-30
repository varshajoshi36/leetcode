'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    single_numbers = []
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            single_numbers.append(nums[i])
            i += 1
        elif nums[i] == nums[i + 1]:
            i += 2
        else:
            single_numbers.append(nums[i])
            i += 1

    return single_numbers


nums = [ 2,3,2,1]
print singleNumber(nums)
