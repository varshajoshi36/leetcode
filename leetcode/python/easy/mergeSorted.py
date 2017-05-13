"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

def merge(nums1, m, nums2, n):
    ind1, ind2 = 0, 0
    for ind1 < m and ind2 < n:
        if numns2[ind2] < nums1[ind1]:
            nums1.insert(ind1, nums[ind2])
            ind1 += 1
        ind1 += 1

    if ind2 < n:
        nums1 += nums2[ind2:]


def merge_inplace(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n -1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n -1] = nums2[n - 1]
            n -= 1           
