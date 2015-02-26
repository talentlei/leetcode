    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0 or x == 1:
            return x
        Max = 46340
        if Max**2 <=x:
            return Max
        low,high = 1,Max**2-1
        while low <=high:
            mid = (low+high)//2
            lmid = mid**2
            hmid = (mid+1)**2
            if x>=lmid and x<hmid:
                return mid
            elif x>lmid:
                low = mid+1
            else:
                high = mid-1
