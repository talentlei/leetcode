    def longestPalindrome(self, s):
        ts = '#'.join(s)
        size = len(ts)
        base = [0 for i in xrange(size)]
        id,i = 0,1
        while i<size:
            if id+base[id]>=i:
                base[i]=min(id+base[id]-i,base[2*id-i])
            while i+base[i]+1<size and i-base[i]-1>=0 and \
                    ts[i+base[i]+1]==ts[i-base[i]-1]:
                    base[i]+=1
            if i+base[i] > id+base[id]:
                id = i
            i+=1
        for i in xrange(size):
            if base[i]>base[id]:
                id=i
        res = ts[id-base[id]:id+base[id]+1]
        return res.replace('#','')
