# @return a list of lists of integer
    def generateMatrix(self, n):
        if n <1:
            return []
        
        result = [[0 for i in range(0,n)] for j in range(0,n)]
        brow,erow = 0,n
        bcol,ecol = 0,n
        count=1
        while brow<erow and bcol <ecol:
            i,j=brow,bcol
            for j in range(bcol,ecol):
                result[i][j]=count
                count+=1
            brow+=1

            for i in range(brow,erow):
                result[i][j]=count
                count+=1
            ecol-=1
            
            for j in range(ecol-1,bcol-1,-1):
                result[i][j]=count
                count+=1
            erow-=1

            for i in range(erow-1,brow-1,-1):
                result[i][j]=count
                count+=1
            bcol+=1
        return result
