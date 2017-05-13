"""
https://leetcode.com/problems/majority-element-ii/#/description
"""

def majorityElement(nums):
    if len(nums) == 0:
        return []
    n = len(nums)
    nums.sort()
    ans = []
    if nums.count(nums[n/3]) > n/3:
        ans.append(nums[n/3])
    if nums.count(nums[(2*n)/3]) > n/3:
        ans.append(nums[(2*n)/3])

    return ans

def main():
    print majorityElement(map(int, raw_input().split(',')))

if __name__ == '__main__':
    main()
