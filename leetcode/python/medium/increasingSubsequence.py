"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""

def findSubsequences(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out_list = []
    for i in range(len(nums) - 1, -1, -1):
        tmp_list = []
        for sub_list in out_list:
            if sub_list[0] >= nums[i]:
                if [[nums[i]] + sub_list] not in out_list and [[nums[i]] + sub_list] not in tmp_list:
                    tmp_list += [[nums[i]] + sub_list]
        if len(tmp_list) > 0:
            out_list += tmp_list
        if [nums[i]] not in out_list:
            out_list.append([nums[i]])

    final_outlist = [x for x in out_list if len(x) > 1]
    return final_outlist

nums = [9, 4, 6, 7, 7]
print nums
print findSubsequences(nums)
