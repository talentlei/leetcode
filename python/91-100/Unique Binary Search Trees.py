    # @return an integer
    def numTrees(self, n):
        if n<2:
            return 1
        num=0
        for i in range(0,n):
            nl = self.numTrees(i)
            nr = self.numTrees(n-i-1)
            if nl==1:
                num += nr
            elif nr==1:
                num += nl
            else:
                num +=nl*nr
        return num
