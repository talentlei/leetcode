    def isLands(self,i,j,grid):
        row,col = len(grid),len(grid[0])
        grid[i][j] = '2'
        if i!=0 and grid[i-1][j]=='1':
            self.isLands(i-1,j,grid)
        if i!=row-1 and grid[i+1][j]=='1':
            self.isLands(i+1,j,grid)
        if j!=0 and grid[i][j-1]=='1':
            self.isLands(i,j-1,grid)
        if j!=col-1 and grid[i][j+1]=='1':
            self.isLands(i,j+1,grid)
        
    # @param grid, a list of list of characters
    # @return an integer
    
    #BFS solution
    def numIslands(self, grid):
        if grid==None or len(grid)==0 or len(grid[0])==0:
            return 0
        row,col=len(grid),len(grid[0])
        counter=0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j]=='1':
                    self.isLands(i,j,grid)
                    counter+=1
        return counter
