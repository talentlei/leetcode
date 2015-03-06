    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        size1,size2,size3 = len(s1),len(s2),len(s3)
        if size3 != size1+size2:
            return False
        record = [[False for i in range(size1+1)] for j in range(size2+1)]
        for i in range(size1):
            if s1[i]==s3[i]:
                record[0][i+1]=True
            else:
                break
        
        for j in range(size2):
            if s2[j]==s3[j]:
                record[j+1][0]=True
            else:
                break
        record[0][0] = True
        for j in range(1,size2+1):
            for i in range(1,size1+1):
                k = i +j
                if s1[i-1]==s3[k-1]:
                    record[j][i] = record[j][i-1] or record[j][i]
                if s2[j-1]==s3[k-1]:
                    record[j][i] = record[j-1][i] or record[j][i]
        return record[size2][size1]
