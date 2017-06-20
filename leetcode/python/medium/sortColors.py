"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    red = []
    white = []
    blue = []

    for item in nums:
        if item == 0:
            red.append(item)
        elif item == 1:
            white.append(item)
        else:
            blue.append(item)

    print red, white, blue
    nums[:len(red)] = red
    nums[len(red): len(red) + len(white)] = white
    nums[len(red) + len(white): len(red) + len(white) + len(blue)] = blue
    print nums

def sortColors2(nums):
    red = nums.count(0)
    white = nums.count(1)
    blue = nums.count(2)

    nums[:red] = [0] * red
    nums[red : red + white] = [1] * white
    nums[red + white : red + white + blue] = [2] * blue

    print nums

nums = [0]
sortColors(nums)
