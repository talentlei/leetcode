class Solution:
    def search(self,i,j,base,word, board):
        base[i][j] =1
        if len(word)<1:
            return True
        up,down,left,right=False,False,False,False
        if i!=0 and base[i-1][j]==0 and word[0]==board[i-1][j]:
            #temp = copy.deepcopy(base)
            up = self.search(i-1,j,base[:],word[1:],board)
            if up:
                return True
        if i!=len(base)-1 and base[i+1][j]==0 and word[0]==board[i+1][j]:
            down = self.search(i+1,j,base[:],word[1:],board)
            if down :
                return True
        if j!=0 and base[i][j-1]==0 and word[0]==board[i][j-1]:
            left = self.search(i,j-1,base[:],word[1:],board)
            if left:
                return True
        if j!=len(base[0])-1 and base[i][j+1]==0 and word[0]==board[i][j+1]:
            right = self.search(i,j+1,base[:],word[1:],board)
            if right :
                return True
        base[i][j]=0   #shallow copy  so need to change back
        return False
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(board)<1 or len(board[0])<1:
            return False
        if len(word)<1:
            return True
        row,col = len(board),len(board[0])
        base = [[0 for j in range(0,col)] for i in range(0,row)]
        for i in range(0,row):
            for j in range(0,col):
                if board[i][j]==word[0]:
                    if self.search(i,j,base[:],word[1:],board):
                        return True
        return False
                        
