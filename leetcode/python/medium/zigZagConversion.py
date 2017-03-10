'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

'''

def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        numColumns = (2*numRows * len(s))/(numRows+1)matrix = []
        for i in range(numRows):
            row = []
            for j in range(numColumns):
                row += [-1]
            matrix += [row]
        index = 0
        rowIndex = 0
        colIndex = 0

        while index < len(s):
            while rowIndex < numRows and index < len(s):
                matrix[rowIndex][colIndex] = index
                rowIndex += 1
                index += 1
            
            rowIndex -= 2
            colIndex += 1
            
            while rowIndex > 0 and index < len(s):
                matrix[rowIndex][colIndex] = index
                rowIndex -= 1
                colIndex += 1
                index += 1


        retString = ""
        rowIndex = 0
        colIndex = 0
        while rowIndex < numRows:
            colIndex = 0
            while colIndex < numColumns:
                if matrix[rowIndex][colIndex] != -1:
                    retString += s[matrix[rowIndex][colIndex]]
                colIndex += 1
            rowIndex += 1


        return retString


string = "PAYPALISHIRING"
print convert(string, 3)
