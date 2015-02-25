class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if not A or len(A) == 1:
            return 0

        cur = 0
        count = 0
        while(cur<len(A)):
            maxReach = -1
            idx = 0
            for i in range(1,A[cur]+1):
                if cur+i >= len(A)-1:
                    return count+1
                else:
                    if A[cur+i] + i > maxReach:
                        maxReach = A[cur+i] + i
                        idx = cur+i
            cur = idx
            count +=1
