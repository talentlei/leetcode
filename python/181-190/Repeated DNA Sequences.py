    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        size=len(s)
        if size<10:
            return []
        Dic={}
        res=[]
        i,t=0,0
        while i<9:
            t=t<<3|ord(s[i])&7
            i+=1
        while i<size:
            t=t<<3& 0x3FFFFFFF|ord(s[i])&7
            if t in Dic:
                res.append(s[i-9:i+1])
            Dic[t]=1
            i+=1
        res=list(set(res))
        return res
