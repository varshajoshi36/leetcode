'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?'''

def uniquePaths( m, n):
	record_path = [[0] * (n + 1)] * (m + 1)
	record_path[m-1][n-1] = 1
	for i in range(m-1,-1,-1):
		for j in range(n-1,-1,-1):
			record_path[i][j] = record_path[i+1][j] + record_path[i][j+1]


	return record_path[0][0]


m,n = 3,4
print uniquePaths( m, n)

