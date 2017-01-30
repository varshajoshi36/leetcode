'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there
'''
def backtracking(row, column, m, n):
        if row is m or n is column:
                return 1
        if row > m or column > n:
                return 0
        return backtracking(row + 1, column, m, n) + backtracking(row, column + 1, m, n)
        
def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        return backtracking(1, 1, m, n)
m, n = 3, 3
print uniquePaths(m, n)
