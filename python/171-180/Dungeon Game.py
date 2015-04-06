    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if len(dungeon)==0 or len(dungeon[0])==0:
            return 0
        row,col=len(dungeon),len(dungeon[0])
        base=[[1 for j in range(col)] for i in range(row)]
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                down,right=1,1
                if j!=col-1 and base[i][j+1]-dungeon[i][j+1]>1:
                    right=base[i][j+1]-dungeon[i][j+1]
                if i!=row-1 and base[i+1][j]-dungeon[i+1][j]>1:
                    down=base[i+1][j]-dungeon[i+1][j]
                if i!=row-1 and j!=col-1:
                    base[i][j]=min(right,down)
                elif i==row-1:
                    base[i][j]=right
                else:
                    base[i][j]=down
        return max(base[0][0]-dungeon[0][0],1)
