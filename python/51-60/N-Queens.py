class Solution:
    result = []
    def isvalid(self,num,value,board):
        for i in range(0,num):
            if value == board[i]:
                return False
            elif value-board[i] == num-i or value-board[i] == i-num:
                return False
        return True
        
    def genSolu(self,board):
        one = []
        size=len(board)
        for i in range(0,size):
            s = '.'*size
            l = list(s)
            l[board[i]]='Q'
            s = ''.join(l)
            one.append(s)
        self.result.append(one)
        
    def getQueue(self,num,board,n):
        if num==n:
            self.genSolu(board)
        for i in range(0,n):
            if self.isvalid(num,i,board):
                board.append(i)
                self.getQueue(num+1,board,n)
                board.pop()
    # @return a list of lists of string
    def solveNQueens(self, n):
        board=[]
        self.getQueue(0,board,n)
        return self.result
        
