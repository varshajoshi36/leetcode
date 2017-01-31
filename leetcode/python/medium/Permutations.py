'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

def permute(nums):
	if len(nums) is 0:
		return []
	permutations = []
	permutations.append([nums[0]])	
	for num in nums[1:]:
		new_perm = []
		for perm in permutations:
			for j in range(len(perm) + 1):
				new_perm.append(perm[:j] + [num] + perm[j:])
		permutations = new_perm

	return permutations

nums = []
print permute(nums)
