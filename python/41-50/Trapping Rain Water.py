class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        A.insert(0,0)
        A.append(0)
        local=[]
        for i in range(1,len(A)-1):
            if A[i]>=A[i-1] and A[i]>=A[i+1]:
                local.append(i)
        if len(local)<2:
            return 0
        capacity=0
        i=0
        while i<len(local)-1:
            j=i+1
            pos=j
            while j<len(local):
                if A[local[j]]>=A[local[i]]:
                    pos = j
                    break
                elif A[local[j]]>A[local[pos]]:
                    pos=j
                j+=1
            shorter = A[local[pos]]
            if A[local[pos]]>A[local[i]]:
                shorter=A[local[i]]
            for p in range(local[i]+1,local[pos]):
                if shorter > A[p]:
                    capacity+=shorter-A[p]
            i=pos
        return capacity
