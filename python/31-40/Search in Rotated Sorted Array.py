class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        size = len(A)
        if size ==0:
            return -1
        if A[0] == target:
            return 0
        for i in range(1,size):
            if A[i] == target:
                return i
            elif A[i] <A[i-1] and target>A[i-1]:
                return -1
        return -1
