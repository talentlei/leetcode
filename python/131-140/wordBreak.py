    def wordBreak(self, s, wordDict):
        if s == None or len(s)==0:
            return true
        size = len(s)
        d = [False for i in xrange(size+1)]
        d[0] = True
        for i in xrange(1,size+1):
            for k in xrange(i):
                if d[k] and s[k:i] in wordDict:
                    d[i] = True
        return d[size]
