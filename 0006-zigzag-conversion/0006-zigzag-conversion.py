class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        row = 0
        direction = 1
        for char in s:
            rows[row] += char
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction

        result = ''.join(rows)
        return result
