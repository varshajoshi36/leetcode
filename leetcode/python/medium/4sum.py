#! /usr/bin/python

def threeSum(nums):

	pos_nums = []
	neg_nums = []
	sol = []
	for i in nums:
		if i < 0:
			neg_nums.append(i)
		else:
			pos_nums.append(i)
	
	if pos_nums.count(0) > 3:
		sol.append([0,0,0,0])

	if len(pos_nums) > 2:
		for i in range(0, len(pos_nums) - 2):
			for j in range(i + 1, len(pos_nums) - 1):
				for k in range(j+1, len(pos_nums)): 
					if -(pos_nums[i] + pos_nums[j] + pos_nums[k]) in neg_nums:
						sol1 = [pos_nums[i], pos_nums[j], pos_nums[k], -(pos_nums[i] + pos_nums[j] + pos_nums[k])]
						if sorted(sol1) not in sol:
							sol.append(sorted(sol1))

	if len(neg_nums) > 2:	
		for i in range(0, len(neg_nums) - 2):
			for j in range(i + 1, len(neg_nums) - 1):
				for k in range(j + 1, len(neg_nums)):
					if -(neg_nums[i] + neg_nums[j] + neg_nums[k]) in pos_nums:
						sol1 = [neg_nums[i], neg_nums[j], neg_nums[k],  -(neg_nums[i] + neg_nums[j] + neg_nums[k])]
						if sorted(sol1) not in sol:
							sol.append(sorted(sol1))
	pos_pair = {}
	neg_pair = {}
	if len(pos_nums) > 1:
		for i in range(0, len(pos_nums) - 1):
			for j in range(i + 1, len(pos_nums)):
				pos_pair[pos_nums[i] +  pos_nums[j]] = [pos_nums[i], pos_nums[j]]

	if len(neg_nums) > 1:
		for i in range(0, len(neg_nums) - 1):
			for j in range(i + 1, len(neg_nums)):
				neg_pair[neg_nums[i] + neg_nums[j]] = [neg_nums[i],  neg_nums[j]]
	

	for pos_num in pos_pair.keys():
		if -pos_num in neg_pair.keys():
			sol1 = pos_pair[pos_num]+neg_pair[-pos_num]
			sol.append(sorted(sol1))
	
		

	return sol

	

nums = [1,0,-1,0,-2,2]
print nums
print threeSum(nums)			

"""

        :type nums: List[int]

        :rtype: List[List[int]]

        """
