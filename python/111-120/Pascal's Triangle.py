    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows<1:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        record = []
        record.append([1])
        record.append([1,1])
        for i in range(2,numRows):
            temp=[1]
            for j in range(len(record[i-1])-1):
                temp.append(record[i-1][j]+record[i-1][j+1])
            temp.append(1)
            record.append(temp)
        return record
