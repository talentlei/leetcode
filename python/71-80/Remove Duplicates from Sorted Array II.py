    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count=1
        i=1
        while i<len(A):
            if A[i]==A[i-1]:
                count+=1
            else:
                count=1
            if count>2:
                count-=1
                i-=1
                del A[i]
            i+=1
        return len(A)
