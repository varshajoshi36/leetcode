"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

def nextPermutation(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 2:
            i = len(nums) - 2
            swapped = False
            while i >= 0:
                if nums[i] < nums[i + 1]:
                    num = nums[i]
                    sorted_rest = sorted(nums[i:])
                    next_large = sorted_rest[len(sorted_rest) - sorted_rest[::-1].index(num)]
                    nums[i] = next_large
                    sorted_rest.remove(next_large)
                    nums[i+1:] = sorted_rest
                    swapped = True
                    break
                i -= 1
            if not swapped:
                nums.sort()
        print nums


