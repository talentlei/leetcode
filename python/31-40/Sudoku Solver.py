class Solution:
    def solve(self,board,row,col):
        for i in range(0,9):
            for j in range(0,9):
                cell = board[i][j]
                if cell == '.':
                    for can in range(1,10):
                        value = str(can)
                        if(self.valid(board,i,j,value)):
                            board[i][j] = value
                            if self.solve(board,i,j):
                                return True
                            board[i][j]='.'
                    return False
        return True
    
    def valid(self,board,i,j,value):
        #check row,col
        for t in range(0,9):
            if board[t][j]==value or board[i][t]==value:
                return False
        #check sqar
        row,col = i//3*3,j//3*3
        for tr in range(row,row+3):
            for tc in range(col,col+3):
                if board[tr][tc]==value:
                    return False
        return True
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solve(board,0,0)
