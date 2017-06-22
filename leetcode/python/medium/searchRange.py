"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]
Its a weird problem. It can be solved using just two python functions.
"""

def searchRange(nums, target):
    if target in nums:
        return [nums.index(target), len(nums)-1-nums[::-1].index(target)]
    else:
        return [-1, -1]
    '''start = 0
    end = len(nums) - 1
    if len(nums) == 0:
        return [-1, -1]   
    if target < nums[0] or target > nums[-1]:
        return [-1, -1]

    range_start = start
    range_end = end

    while start < end:
        mid = (start + end)/2
        print start, end
        print 'mid', mid
        if nums[mid] == target:
            print "in == target"
            if mid != 0 and mid != len(nums) - 1:
                if nums[mid + 1] == target:
                    return [mid, mid + 1]
                elif nums[mid - 1] == target:
                    return [mid -1, mid]
                else:
                    return [mid, mid]
            if mid == 0:
                if nums[1] == target:
                    return [0, 1]
                else:
                    return [0, 0]
            if mid == len(nums) - 1:
                if nums[mid - 1] == target:
                    return [mid -1, mid]
                else:
                    return [mid, mid]
        if nums[mid] < target:
            range_start = mid
            start = mid + 1
        else:
            if range_start < range_end - 1:
                if nums[mid - 1] >= target:
                    range_end = mid
                else:
                    range_end = mid
            end = mid
            
        print "**", start, end

    return [range_start, range_end]'''

def main():
	nums = map(int, raw_input().split(','))
	target = int(raw_input())
	print searchRange(nums, target)

if __name__ == "__main__":
    main()
