class Solution:
    res = [] 
    def getResult(self,s,d,one,ind):
        for i in d[ind][1:]:
            if i == -1:
                self.res.append(one)
                return
            one.append(s[i:ind])
            self.getResult(s,d,one[:],i);
            one.pop()
        
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]     
    def wordBreak(self, s, wordDict):
        if s == None or len(s)==0:
            return true
        size = len(s)
        d = [[False] for i in xrange(size+1)]
        d[0][0] = True
        d[0].append(-1)
        for i in xrange(1,size+1):
            for k in xrange(i):
                if d[k][0] and s[k:i] in wordDict:
                    d[i][0] = True
                    d[i].append(k)
        if not d[size][0]:
            return []
            
        one = []
        self.getResult(s,d,one,size)
        re = []
        for data in self.res:
            data.reverse()
            re.append(' '.join(data))
        return re
