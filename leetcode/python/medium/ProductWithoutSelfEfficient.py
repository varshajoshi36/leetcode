'''Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

'''

def productExceptSelf(nums):
	output_array = [1] * len(nums)
	
	for i in range(1,len(nums)):
		output_array[i] = output_array[i - 1] * nums[i - 1]
		
	left = 1
	for i in range(len(nums) - 1, -1, -1):
		output_array[i] *= left
		left *= nums[i]

	return output_array

nums = [1,2,3,4]
print productExceptSelf(nums)
