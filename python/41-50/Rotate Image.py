class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n=len(matrix)
        ceng=0
        while ceng<n//2:
            pos = ceng
            while pos <n-ceng-1:
                temp=matrix[ceng][pos]
                matrix[ceng][pos]=matrix[n-pos-1][ceng]
                matrix[n-pos-1][ceng]=matrix[n-ceng-1][n-pos-1]
                matrix[n-ceng-1][n-pos-1]=matrix[pos][n-ceng-1]
                matrix[pos][n-ceng-1]=temp
                pos+=1
            ceng+=1
        return matrix
