    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix)<0 or len(matrix[0])<0:
            return False
        row,col=len(matrix),len(matrix[0])
        low,high=0,row*col-1
        while low <=high:
            mid = (low+high)//2
            i,j=mid//col,mid%col
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                high = mid-1
            else :
                low = mid+1
        return False
