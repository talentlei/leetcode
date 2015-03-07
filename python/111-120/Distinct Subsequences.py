    # @return an integer
    def numDistinct(self, S, T):
        ss,st=len(S),len(T)
        if ss<st:
            return 0
        if S==T or T=='':
            return 1
        record = [ [0 for j in range(ss+1)] for i in range(st+1)]
        for j in range(ss+1):
            record[0][j]=1
        for i in range(1,st+1):
            for j in range(1,ss+1):
                if S[j-1]==T[i-1]:
                    record[i][j]=record[i-1][j-1]+record[i][j-1]
                else:
                    record[i][j]=record[i][j-1]
        return record[st][ss]
