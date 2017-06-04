"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
"""

def convertToBase7(num):
    if num < 0:
        sign = "-"
        num = num * -1
    else:
        sign = ""
    base_seven = ""
    while num > 0:
        sevit = num % 7
        base_seven = str(sevit) + base_seven
        num = num/7

    return sign + base_seven

num = -100
print convertToBase7(num)
