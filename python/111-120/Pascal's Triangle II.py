    # @return a list of integers
    def getRow(self, rowIndex):
        rowIndex+=1
        if rowIndex<1:
            return []
        if rowIndex==1:
            return [1]
        record=[1,1]
        for i in range(2,rowIndex):
            temp=[1]
            for j in range(len(record)-1):
                temp.append(record[j]+record[j+1])
            temp.append(1)
            record=temp
        return record
