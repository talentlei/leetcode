    # @return a list of integers
    def grayCode(self, n):
        result=[0]
        for i in range(0,n):
            inc = 1<<i
            for j in range(len(result)-1,-1,-1):
                result.append(result[j]+inc)
        return result
