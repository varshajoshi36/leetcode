'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
'''

def nextGreaterElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 0:
        return []
    out_list = ['*'] * len(nums)
    trail_ele = []

    for i in range(len(nums)):
        if len(trail_ele) == 0:
            trail_ele.append((i, nums[i]))
            continue
        while nums[i] > trail_ele[-1][1]:
            out_list[trail_ele[-1][0]] = nums[i]
            trail_ele.pop()
            if len(trail_ele) == 0:
                break
        trail_ele.append((i, nums[i]))

    print trail_ele
    i = 0
    while i < len(nums) and len(trail_ele) > 1:
        while nums[i] > trail_ele[-1][1]:
            out_list[trail_ele[-1][0]] = nums[i]
            trail_ele.pop()
        i += 1
    for ele in trail_ele:
        out_list[ele[0]] = -1
    return out_list

nums = [2,1]
print nums
print nextGreaterElements(nums)


