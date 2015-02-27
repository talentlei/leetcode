    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        size = len(A)
        if size<=1:
            return
        record=[0,0,0]
        for i in A:
            record[i]+=1
        record[1] +=record[0]
        record[2] +=record[1]
        for i in range(0,size):
            if i < record[0]:
                A[i]=0
            elif i <record[1]:
                A[i]=1
            else :
                A[i]=2
        return 
