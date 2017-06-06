"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]
"""

def traverseRight(matrix, x, y):
    len_limit = len(matrix[0])
    hei_limit = len(matrix)

    if x >= hei_limit or y >= len_limit or matrix[x][y] == None:
        return [], -1, -1

    elements = []
    while y < len_limit:
        if y == len_limit - 1:
            return elements, x, y
        elif matrix[x][y+1] == None:
            return elements, x, y
        elements.append(matrix[x][y])
        matrix[x][y] = None
        y += 1

def traverseDown(matrix, x, y):
    len_limit = len(matrix[0])
    hei_limit = len(matrix)

    if x >= hei_limit or y >= len_limit or matrix[x][y] == None:
        return [], -1, -1

    elements = []
    while x < hei_limit:
        if x == hei_limit - 1:
            return elements, x, y
        elif matrix[x+1][y] == None:
            return elements, x, y
        elements.append(matrix[x][y])
        matrix[x][y] = None
        x += 1

def traverseLeft(matrix, x, y):
    len_limit = len(matrix[0])
    hei_limit = len(matrix)

    if x >= hei_limit or y >= len_limit or matrix[x][y] == None:
        return [], -1, -1

    elements = []
    while y >= 0:
        if y == 0:
            return elements, x, y
        elif matrix[x][y-1] == None:
            return elements, x, y
        elements.append(matrix[x][y])
        matrix[x][y] = None
        y -= 1

def traverseUp(matrix, x, y):
    len_limit = len(matrix[0])
    hei_limit = len(matrix)

    if x >= hei_limit or y >= len_limit or matrix[x][y] == None:
        return [], -1, -1

    elements = []
    while x >= 0:
        if x == 0:
            return elements, x, y
        elif matrix[x-1][y] == None:
            return elements, x, y
        elements.append(matrix[x][y])
        matrix[x][y] = None
        x -= 1 

def spiralOrder(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    spiral_elements = []
    x, y = 0, 0
    while 1:
        elements, x, y = traverseRight(matrix, x, y)
        spiral_elements += elements
        if len(elements) == 0 and x == len(matrix) - 1:
            return spiral_elements + [matrix[x][y]]
        elements, x, y = traverseDown(matrix, x, y)
        spiral_elements += elements
        if len(elements) == 0:
            return spiral_elements + [matrix[x][y]]
        elements, x, y = traverseLeft(matrix, x, y)
        spiral_elements += elements
        if len(elements) == 0:
            return spiral_elements + [matrix[x][y]]
        elements, x, y = traverseUp(matrix, x, y)
        spiral_elements += elements
        if len(elements) == 0:
            return spiral_elements + [matrix[x][y]]
    
matrix = [[1,2], [4,5]]
for el in matrix:
    print el
print spiralOrder(matrix)
