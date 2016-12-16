#! /usr/bin/python

def fourSumTarget(nums, target):
	sol = []
	nums = sorted(nums)
	for i in range(0, len(nums) - 3):
		print 'in for'
		for j in range(i+1, len(nums) - 2):
			p = j + 1
			q = len(nums) - 1
			print p,q
			while(p < q):
				tmp_sum = nums[i] + nums[j] + nums[p] + nums[q]
				if(target == tmp_sum):
					sol1 = [nums[i],  nums[j],  nums[p],  nums[q]]
					print sol1
					p += 1
					q -= 1
					if sorted(sol1) not in sol:
						sol.append(sol1)
				elif(target > tmp_sum):
					p += 1
				else:
					q -= 1

        return sol


target, nums = 0, [0,0,0]
print target, nums
print fourSumTarget(nums, target)
