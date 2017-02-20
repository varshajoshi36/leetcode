

def rotateMatrix(matrix):
	if len(matrix) is 0:
		return
	#clockwise
	new_row, new_column = len(matrix[0]), len(matrix)

	clockwise_matr = []
	for j in range(new_row):
		row = []
		for i in range(new_column):
			row = [matrix[i][j]] + row
		clockwise_matr = clockwise_matr + [row]

	print "Clock: "
	for i in range(len(clockwise_matr)):
		print clockwise_matr[i]
	
	#anticlockwise
	anticlock_matrix = []
	for j in range(new_row - 1, -1, -1):
		row = []
		for i in range(new_column):
			row = row + [matrix[i][j]]
		anticlock_matrix = anticlock_matrix + [row]

	print"anti:"
	for i in range(len(anticlock_matrix)):
	        print anticlock_matrix[i]


matrix = [[1, 2,  3], 
 [5,  6,  7],
 [9, 10, 11],
[13, 14, 15]]
'''matrix = [[1, 2, 3],
[4,  5,  6],
 [7,  8,  9]]'''
for i in range(len(matrix)):
	print "original: ", matrix[i]
rotateMatrix(matrix)

