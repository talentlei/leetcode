class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        
        #check row
        for row in board:
            record=[0 for i in range(0,9)]
            for cell in row:
                if cell =='.':
                    continue
                if record[int(cell)-1]!=1:
                    record[int(cell)-1] =1
                else:
                    return False
            record=[]

        #check col
        for j in range(0,9):
            record=[0 for k in range(0,9)]
            for i in range(0,9):
                cell = board[i][j]
                if cell =='.':
                    continue
                if record[int(cell)-1]!=1:
                    record[int(cell)-1]=1
                else:
                    return False
            record =[]
        #check sqar
        for i in range(0,9,3):
            for j in range(0,9,3):
                record=[0 for k in range(0,9)]
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        cell = board[row][col]
                        if cell =='.':
                            continue
                        if record[int(cell)-1]!=1:
                            record[int(cell)-1]=1
                        else:
                            return False
                record=[]
        return True
