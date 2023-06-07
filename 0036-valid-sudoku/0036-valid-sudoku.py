class Solution:
    def __init__(self) -> None:
        pass

    def check_row(self, row: list[str]) -> bool:
        row = [i for i in row if i != "."]
        return len(row) == len(set(row))


    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # Check rows
        for row in board:
            if not self.check_row(row):
                print("Row failed")
                return False
        
        # Check col
        for col in range(9):
            deneme = [board[i][col] for i in range(9)]
            if not self.check_row(deneme):
                print("col failed")
                return False
            
        # Check square
        colL = 0
        for k in range(0,9):
            rowL = (3 * (k)) % 9
            if (k+1) % 3 == 0 and k != 0:
                colL = (colL + 3) % 9
            print("colL: ", colL)
            print("rowL: ", rowL)
            deneme = [board[i+colL][j+rowL] for i in range(3) for j in range(3)]
            print(deneme)
            if not self.check_row(deneme):
                print("square failed")
                return False
        
        return True