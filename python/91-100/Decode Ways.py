    def subDecodings(self,s):
        if s in self.dic:
            return self.dic[s]
        if len(s)==0 or  (len(s)==1 and s!='0'):
            return 1
        if s[0]=='0':
            return 0
        one,two = 0,0
        one = self.subDecodings(s[1:])
        if s[0:2]>='10' and s[0:2]<='26':
            two = self.subDecodings(s[2:])
        self.dic[s]=one + two
        return one+two
    # @param {string} s
    # @return {integer}
    dic={}
    def numDecodings(self, s):
        if s==None or len(s)==0 or s[0]=='0':
            return 0
        for i in xrange(1,len(s)):
            if s[i]=='0':
                if s[i-1]!='1' and s[i-1]!='2':
                    return 0
        return self.subDecodings(s)
