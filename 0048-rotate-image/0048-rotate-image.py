class Solution:
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        for c in range(col):
            tut = None
            for r in range(c, row):
                tut = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tut

        rev = 0
        for r in range(row):
            for c in range(col // 2):
                rev = matrix[r][c]
                matrix[r][c] = matrix[r][col - c - 1]
                matrix[r][col - c - 1] = rev

        print(matrix)
        return matrix
