    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        rows = len(triangle)
        if rows <1:
            return 0
        record = [0 for i in range(rows)]
        nrecord = []
        for i in range(0,rows):
            for j in range(0,len(triangle[i])):
                if j==0:
                    nrecord.append(record[j]+triangle[i][j])
                elif j==i:
                    nrecord.append(record[j-1]+triangle[i][j])
                else:
                    nrecord.append(min(record[j-1],record[j])+triangle[i][j])
            record=nrecord
            nrecord=[]
        Min = record[0]
        for i in range(rows):
            if record[i]<Min:
                Min=record[i]
        return Min
