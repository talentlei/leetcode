    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        size = len(A)
        if size ==0:
            return False
        if A[0] == target:
            return True
        for i in range(1,size):
            if A[i] == target:
                return True
            elif A[i] <A[i-1] and target>A[i-1]:
                return False
        return False
