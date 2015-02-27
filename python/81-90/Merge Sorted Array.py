    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        result=[]
        ap,bp=0,0
        while ap<m and bp<n:
            if A[ap]<B[bp]:
                result.append(A[ap])
                ap+=1
            else:
                result.append(B[bp])
                bp+=1
        if ap!=m:
            result+=A[ap:]
        else:
            result+=B[bp:]
        for i in range(0,m+n):
            A[i]=result[i]
        return
