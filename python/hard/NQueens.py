size = 0
chess_board = []
rows = []


def check_diagonals( x, y):
	dia_clear = True
	row, col = x, y
	while row >= 0 and col >= 0:
		if chess_board[row][col] is not 2 or chess_board[row][col] is not 1:
			row -= 1
			col -= 1
		else:
			return False
		
	row, col = x, y
	while row >= 0 and col > size:
		if chess_board[row][col] is not 2 or chess_board[row][col] is not 1:
			row -= 1
			col += 1
		else:
			return False

	row, col = x, y
	while row < size and col >= 0:
		if chess_board[row][col] is not 2 or chess_board[row][col] is not 1:
			row += 1
			col -= 1
		else:
			return False

	row, col = x, y
	while row < size and col < size:
		if chess_board[row][col] is not 2 or chess_board[row][col] is not 1:
			row += 1
			col += 1
		else:
			return False

	return True

def check_column( x, y):
	for i in range(size):
		if chess_board[i][y] is 2 or chess_board[i][y] is 1:
			return False

	return True

			
def find_spot( row):
	for col in range(size):
		if chess_board[row][col] is not 2 and check_column(row, col) and check_diagonals(row, col):
			return col
	return -1
			
			
def place_queens( row):
	if 0 not in chess_board[row]:
		return False

	global chess_board, rows

	spot_x = row
	spot_y = find_spot(row)
	if spot_y is -1:
		return False
	chess_board[spot_x][spot_y] = 1
	rows.remove(row)
	for next_row in rows:
		if place_queens(next_row) is False:
			chess_board[spot_x][spot_y] = 2
			rows.insert(0, row)
			place_queens(row)
		else:
			return True

def startq():
	global size, chess_board, rows 
	size = 4
	chess_board = [[0] * size] * size
	x, y = 2, 1
	rows = range(0,size)
	chess_board[x-1][y-1] = 1
	rows.remove(x)
	if place_queens(rows[0]) is True:
		for i in range(size):
			print chess_board[i]

	else:
		print "No Solution"					



startq() 

