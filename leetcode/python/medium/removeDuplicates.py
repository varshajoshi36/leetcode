"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    last_element = nums[-1]
    last_element_count = nums.count(last_element)
    count = 1
    i = 1
    while i < len(nums) and nums[i] != last_element:
        if nums[i] == nums[i-1]:
            count += 1
            if count > 2:
                nums[i:] = nums[i+1:] + [0]
                i -= 1
        else:
               count = 1
        i += 1
    last_index = nums.index(last_element)
    if last_element_count > 1:
        return last_index + 2
    else:
        return last_index + 1

# from leetcode
def shortRemoveDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    print nums
    return i

nums = [1,1,1,2,2,2]
print shortRemoveDuplicates(nums)
