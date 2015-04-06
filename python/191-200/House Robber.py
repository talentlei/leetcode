    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        size=len(num)
        if size<1:
            return 0
        if size==1:
            return num[0]
        base=[ 0 for i in range(size)]
        base[0]=num[0]
        base[1]=max(num[0],num[1])
        for i in range(2,size):
            base[i]=max(base[i-2]+num[i],base[i-1])
        return base[size-1]
