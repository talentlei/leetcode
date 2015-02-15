class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        size = len(A)
        if size ==0:
            return 0
        left,right = 0,size-1
        while left <=right:
            mid = (left+right)/2
            if A[mid]==target:
                return mid
            elif A[mid]<target:
                if mid==size-1 or A[mid+1]>target:
                    return mid+1
                left = mid+1
            else:
                if mid ==0 or A[mid-1]<target:
                    return mid
                right = mid-1
