   # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        size = len(A)
        if not A:
            return True
        isReach = [0 for i in range(0,size)]
        isReach[0] = 1
        Max=0
        for i in range(0,size):
            if isReach[i]==1:
                if i+A[i]>=size-1:
                    return True
                elif i+A[i]>Max:
                    Max=i+A[i]
                    for j in range(i+1,Max+1):
                        isReach[j]=1
        return False
