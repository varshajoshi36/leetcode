#https://www.hackerrank.com/challenges/grid-challenge

no_test = int(raw_input()) 

for i in range(no_test):
	grid = []
	size = int(raw_input())
	for j in range(size):
		row = list(str(raw_input()))
		row.sort()
		grid += [row]

	col_ind = 0
	flag = True
	while col_ind < size and flag:
		row_ind = 1
		while row_ind < size:
			if grid[row_ind][col_ind] < grid[row_ind -1][col_ind]:
				print "NO"
				flag = False
				break
			row_ind += 1
		col_ind += 1
	if flag:
		print "YES"
