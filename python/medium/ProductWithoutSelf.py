'''Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

'''

def productExceptSelf(nums):
	output_array = [1] * len(nums)
	for index in range(len(nums)):
		output_array[0 : index] = [x * nums[index] for x in output_array[0 : index]]
		output_array[index + 1 : len(nums)] = [x * nums[index] for x in output_array[index + 1 : len(nums)]]

	return output_array

nums = [1,2,3,4]
print productExceptSelf(nums)
