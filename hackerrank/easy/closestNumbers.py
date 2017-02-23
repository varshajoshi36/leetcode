#https://www.hackerrank.com/challenges/closest-numbers
import sys

n = int(raw_input())

nums = map(int, raw_input().split())

nums.sort()

min_diff = sys.maxint
ret_list = []
for i in range(1, n):
	diff = nums[i] - nums[i - 1]
	if diff < min_diff:
		min_diff = diff
		ret_list = [nums[i - 1], nums[i]]
	elif diff == min_diff:
		ret_list += [nums[i - 1], nums[i]]

print ' '.join(map(str, ret_list))

