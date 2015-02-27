    def sub(self,S,pos):
        result=[[],[S[pos]]]
        if pos+1==len(S):
            return result
        tempr = self.sub(S,pos+1)
        result = [[S[pos]]+i for i in tempr]
        result.extend(tempr)
        return result
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        result=[]
        if len(S)<1:
            return result
        S.sort()
        result = self.sub(S,0)
        pos =0
        while pos <len(result):
            if result[pos] in result[:pos]:
                del result[pos]
            else:
                pos+=1
        return result
