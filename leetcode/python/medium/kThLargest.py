"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length
"""

class Solution(object):
    def quickPartition(self, nums, start, end):
    	pivote = nums[start]
	l, r = start + 1, end
	while l <= r:
		if nums[l] <= pivote and nums[r] > pivote:
			nums[l], nums[r] = nums[r], nums[l]
		if nums[l] > pivote:
			l += 1
		if nums[r] <= pivote:
			r += 1
	nums[start], nums[r] = nums[r], nums[start]
	return r

    def findKthLargest(self, nums, k):
    	start, end = 0, len(nums) -1
	while True:
		pos = self.quickPartition(nums, start, end)
		if pos == k-1:
			return nums[pos]
		if pos > k - 1:
			start = pos -1
		else:
			end = pos + 1
