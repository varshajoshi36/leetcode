'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
'''

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    return nums[-k:] + nums[:len(nums) - k]
    
# Fails test case of [1,2] 3
def rotateInPlace(nums, k):
    length = len(nums)
    ks = []
    while k > length:
        k = k - length
        ks.append(length)
        if k < length:
            ks.append(k)
    
    for k in ks:
        if k != length:
            b = nums[-k:]
            nums[-k:] = nums[-2 * k: -k]
            nums[-(k) - (length - 2 * k):-(k)] = nums[:length - 2*k]
            nums[:k] = b

def rotateInPlace(nums, k):
    length = len(nums)
    for i in range(k):
        b = nums[-1]
        nums[1:] = nums[:length - 1]
        nums[0] = b
