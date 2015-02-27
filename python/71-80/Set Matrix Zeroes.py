    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return 
        row,col = len(matrix),len(matrix[0])
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==0:
                    for p in range(0,row):
                        if matrix[p][j] != 0:
                            matrix[p][j]='0'
                    for p in range(0,col):
                        if matrix[i][p] != 0:
                            matrix[i][p]='0'
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]=='0':
                    matrix[i][j]=0
