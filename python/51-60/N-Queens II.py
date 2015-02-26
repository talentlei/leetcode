class Solution:
    result=0
    def isvalid(self,num,value,board):
        for i in range(0,num):
            if value == board[i]:
                return False
            elif value-board[i] == num-i or value-board[i] == i-num:
                return False
        return True

    def getQueue(self,num,board,n):
        if num==n:
            self.result+=1
        for i in range(0,n):
            if self.isvalid(num,i,board):
                board.append(i)
                self.getQueue(num+1,board,n)
                board.pop()
    # @return an integer
    def totalNQueens(self, n):
        board=[]
        self.getQueue(0,board,n)
        return self.result
