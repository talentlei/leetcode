    # @return an integer
    def uniquePaths(self, m, n):
        if m==1 or n==1:
            return 1
        record=[[1 for j in range (0,n)]  for i in range(0,m)]
        
        for i in range(1,m):
            for j in range(1,n):
                record[i][j]=record[i-1][j]+record[i][j-1]
        return record[m-1][n-1]
