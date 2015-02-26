    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m,n=len(grid),len(grid[0])
        record=[[0 for j in range (0,n)]  for i in range(0,m)]
        
        record[0][0]=grid[0][0]
        for i in range(1,m):
            record[i][0] = record[i-1][0]+grid[i][0]
        for j in range(1,n):
            record[0][j] = record[0][j-1]+grid[0][j]
            
        for i in range(1,m):
            for j in range(1,n):
                shorter = record[i-1][j]
                if record[i][j-1]<record[i-1][j]:
                    shorter = record[i][j-1]
                record[i][j]=shorter+ grid[i][j]
        return record[m-1][n-1]
