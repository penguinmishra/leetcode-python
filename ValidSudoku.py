# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isPlaceable(self, board: list[list[str]], i: int, j: int, no: str, n: int) -> bool:
        for k in range(0, j):
            if board[i][k] == no:
                return False
        for k in range(j + 1, n):
            if board[i][k] == no:
                return False
        for k in range(0, i):
            if board[k][j] == no:
                return False
        for k in range(i + 1, n):
            if board[k][j] == no:
                return False
        
        sx = (i // 3) * 3
        sy = (j // 3) * 3

        for x in range(sx, sx + 3):
            for y in range(sy, sy + 3):
                if x != i and y != j and board[x][y] == no:
                    return False
        return True

    

    def isValid(self, board: list[list[str]], i: int, j: int, n: int) -> bool:
        if i == n:
            return True
        if j == n:
            return self.isValid(board, i + 1, 0, n)
        if board[i][j] == '.':
            return self.isValid(board, i, j + 1, n)
        if not self.isPlaceable(board, i, j, board[i][j], n):
            return False
        return self.isValid(board, i, j + 1, n)



    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.isValid(board, 0, 0, len(board))


if __name__ == '__main__':
    validSudoku = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(validSudoku.isValidSudoku(board))