"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""
class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		sol = []
		self.dfs(candidates, 0, sol, [], target)
		return sol
		


	def dfs(self, nums, index, sol, local_sol, remaining):
		if remaining < 0:
			return
		if remaining == 0:
			sol.append(local_sol)
			return
		else:
			for i in range(index, len(nums)):
				self.dfs(nums, i, sol, local_sol+[nums[i]], remaining-nums[i])
		
if __name__ == '__main__':
	obj = Solution()
	candidates, target = [2,3,6,7], 7
	print "Input:", candidates, target
	print "Solution:", obj.combinationSum(candidates, target)
