import math

def constructRectangle(area):
    pivote = math.sqrt(area)
    for i in range(int(pivote), 0, -1):
        if area % i == 0:
            return [area/i, i]

area = 9
print area
print constructRectangle(area)
