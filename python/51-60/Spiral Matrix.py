class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result =[]
        if not matrix or not matrix[0]:
            return result
        brow,erow = 0,len(matrix)
        bcol,ecol = 0,len(matrix[0])
        while brow<erow and bcol <ecol:
            i,j=brow,bcol
            for j in range(bcol,ecol):
                result.append(matrix[i][j])
            brow+=1
            
            if brow == erow:
                break
            for i in range(brow,erow):
                result.append(matrix[i][j])
            ecol-=1
            
            if ecol == bcol:
                break
            for j in range(ecol-1,bcol-1,-1):
                result.append(matrix[i][j])
            erow-=1
            
            if erow==brow:
                break
            for i in range(erow-1,brow-1,-1):
                result.append(matrix[i][j])
            bcol+=1
        return result
