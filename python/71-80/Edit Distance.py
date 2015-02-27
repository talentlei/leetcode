    # @return an integer
    def minDistance(self, word1, word2):
        m,n=len(word1),len(word2)
        record = [[0 for j in range(0,m+1)] for i in range(0,n+1)]
        for j in range(0,m+1):
            record[0][j]=j
        for i in range(0,n+1):
            record[i][0]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word2[i-1]==word1[j-1]:
                    record[i][j]=record[i-1][j-1]
                else:
                    record[i][j]=min(record[i-1][j-1],min(record[i][j-1],record[i-1][j]))+1
        return record[n][m]
