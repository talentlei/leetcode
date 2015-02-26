    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        record=[[0 for j in range (0,n)]  for i in range(0,m)]
        for i in range(0,m):
            if obstacleGrid[i][0]==1:
                break
            record[i][0]=1
        
        for j in range(0,n):
            if obstacleGrid[0][j]==1:
                break
            record[0][j]=1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid [i][j]==1:
                    record[i][j]=0
                    continue
                record[i][j]=record[i-1][j]+record[i][j-1]
        return record[m-1][n-1]
