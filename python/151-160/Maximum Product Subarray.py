    def maxProduct(self, A):
        size= len(A)
        if size==1:
            return A[0]
        Max=[A[0]]
        Min=[A[0]]
        for i in range(1,size):
            Max.append(max(max(Max[i-1]*A[i],Min[i-1]*A[i]),A[i]))
            Min.append(min(min(Max[i-1]*A[i],Min[i-1]*A[i]),A[i]))
        tmax=Max[0]
        for i in range(0,size):
            if Max[i]>tmax:
                tmax=Max[i]
        return tmax
