"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sol = []
        candidates.sort()
        self.dfs(candidates, 0, sol, [], target)
        return sol

    def dfs(self, nums, index, sol, local_sol, remaining):
        if remaining < 0:
            return
        if remaining == 0:
            sol.append(sorted(local_sol))
            return
        else:
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]: continue
                self.dfs(nums, i+1, sol, local_sol+[nums[i]], remaining-nums[i])



if __name__ == '__main__':
        obj = Solution()
        candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
        print "Input:", candidates, target
        print "Solution:", obj.combinationSum2(candidates, target)

