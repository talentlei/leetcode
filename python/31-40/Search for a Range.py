class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        size = len(A)
        if(A ==0):
            return [-1,-1]
        index=[]
        left,right = 0,size-1
        #find left
        while left <=right:
            mid = (left+right)/2
            if A[mid]==target and (mid==0 or A[mid-1]!=A[mid]):
                index.append(mid)
                break
            elif A[mid]<target:
                left = mid+1
            else:
                right = mid-1
        #judge
        if not index:
            return [-1,-1]
        left,right = 0,size-1
        #find right
        while left <=right:
            mid = (left+right)/2
            if A[mid]==target and (mid==size-1 or A[mid+1]!=A[mid]):
                index.append(mid)
                break
            elif A[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return index
