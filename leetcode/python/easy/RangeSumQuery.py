

class NumArray(object):
    sum_cumulative = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) is not 0:
            self.sum_cumulative = [0] * len(nums)
            self.sum_cumulative[0] = nums[0]
            for i in range(1, len(nums)):
                self.sum_cumulative[i] = self.sum_cumulative[i - 1] + nums[i]        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(self.sum_cumulative) is 0:
            return 0
        if i is 0:
            return self.sum_cumulative[j]
        return self.sum_cumulative[j] - self.sum_cumulative[i -1] 
        
# Your NumArray object will be instantiated and called as such:
i, j = [-2, 0, 3, -5, 2, -1],[0,2]
obj = NumArray(i)
param_1 = obj.sumRange(0, 2)
print param_1
