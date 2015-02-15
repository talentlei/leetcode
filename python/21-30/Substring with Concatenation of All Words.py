# need to optimize
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        result = []
        if not L or not S:
            return result
        ldic = {}
        for word in L:
            if word in ldic:
                ldic[word]+=1
            else:
                ldic[word]=1
             
        size = len(L[0])
        num = len(ldic)
        for start in range(0,size):
            record = {}
            temp ,begin= 0,start
            i = start
            while i+size <= len(S):
                word = S[i:i+size]
                if word in ldic:
                    if not record:
                        begin = i
                    if word not in record or record[word]<ldic[word]:
                        if word not in record:
                            record[word] = 1
                        else:
                            record[word] +=1
                        if record[word]==ldic[word]:
                            temp+=1
                        i +=size
                        if temp!=num:
                            continue
                        else:
                            result.append(begin)
                record={}
                temp=0
                i = begin+size
                begin =i
        return result
