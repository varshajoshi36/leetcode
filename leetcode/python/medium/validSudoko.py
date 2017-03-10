'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

def isValidCube(board):
    isValidCube = True
    startRow = 0
    endRow = 2
    step = 3
    while endRow < len(board):
        startCol = 0
        endCol = 2
        while endCol < len(board):
            subMatr = [item[startCol : endCol + 1] for item in board[startRow : endRow + 1]]
            for i in range(len(subMatr)):
                for j in range(len(subMatr[0])):
                    for line in range(i + 1, len(subMatr)):
                        if subMatr[i][j] != '.' and subMatr[i][j] in subMatr[line]:
                            return False
            startCol += step
            endCol += step
        startRow += step
        endRow += step

    return True


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    isValid = True
    numRows = len(board)
    if numRows == 0:
        return True
    numCol = len(board[0])

    colBoard = []
    for i in range(numCol):
        col = ""
        for j in range(numRows):
            col += board[j][i]
        colBoard += [col]
    for i in range(numRows):
        print board[i]
    for i in range(numRows):
        for j in range(numCol):
            if board[i][j] in board[i][j + 1:] and board[i][j] != '.':
                isValid = False

    for i in range(numCol):
        for j in range(numRows):
            if colBoard[i][j] in colBoard[i][j + 1:] and colBoard[i][j] != '.':
                isValid = False
    if isValid and isValidCube(board):
        return True
    else:
        return False


board = ["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]
print isValidSudoku(board)
