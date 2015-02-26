    def climbStairs(self, n):
        if n == 1:
            return 1
        record = [0 for i in range(0,n)]
        record[0] =1 
        record[1] =2
        for i in range(2,n):
            record[i]=record[i-1]+record[i-2]
        return record[n-1]
