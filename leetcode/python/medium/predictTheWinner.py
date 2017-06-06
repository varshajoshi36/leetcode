"""
Not working. gives the best strategy
"""

import numpy as np

def optimalStrategyOfGame(nums):
    n = len(nums) 
    table = [[None for i in range(n)] for i in range(n)]

    for gap in range(n):
        i = 0
        j = gap
        while j < n:
            
            x = table[i+2][j] if (i+2) <= j else 0
            y = table[i+1][j-1] if (i+1) <= (j-1) else 0
            z = table[i][j-2] if i <= (j-2) else 0

            table[i][j] = max(nums[i] + min(x, y), nums[j] + min(y,z))

            i += 1
            j += 1

    return table[0][n-1]


def predictTheWinner(nums):
    optimalScore = optimalStrategyOfGame(nums)
    if optimalScore > sum(nums) - optimalScore:
        return True
    else:
        return False

nums = [1, 5, 233, 7]
print nums
optimal = predictTheWinner(nums)
print "optimal", optimal
