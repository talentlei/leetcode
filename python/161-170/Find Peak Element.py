    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        size = len(num)
        if size <2:
            return size-1
        if num[0]>num[1]:
            return 0
        if num[-1]>num[-2]:
            return size-1
        for i in range(1,size-1):
            if num[i]>num[i-1] and num[i]>num[i+1]:
                return i
        return -1
