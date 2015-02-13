class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = len(A)+len(B)
        if l%2==1:
            return self.kth(A,B,l/2)
        else:
            return (self.kth(A,B,l/2)+self.kth(A,B,l/2-1))/2.
            
    def kth(self,A,B,k):
        if not A:
            return B[k]
        if not B:
            return A[k]
        ia,ib = len(A)/2,len(B)/2
        ma,mb = A[ia],B[ib]
        
        if ia+ib <k:
            if ma>mb:
                return self.kth(A,B[ib+1:],k-ib-1)
            else:
                return self.kth(A[ia+1:],B,k-ia-1)
        else:
            if ma >mb:
                return self.kth(A[:ia],B,k)
            else:
                return self.kth(A,B[:ib],k)
