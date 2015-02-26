    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        Max,temp=A[0],0
        for i in range(0,len(A)):
            temp+=A[i]
            if temp>Max:
                Max=temp
            if temp<0:
                temp=0
        return Max
