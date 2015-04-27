class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    dic={}
    def isMatch(self, s, p):
        if (s,p) in self.dic:
            return self.dic[(s,p)]
        if p==None or p=='':
            self.dic[(s,p)] = p==s
            return p==s
        elif len(p)==1:
            self.dic[(s,p)] = len(s)==1 and(s==p or p=='.')
            return len(s)==1 and(s==p or p=='.')
        if p[1]!='*':
            self.dic[(s,p)]=len(s)>0 and(s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:],p[1:])
            return len(s)>0 and(s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:],p[1:])
        i=0
        while len(s)>i and (s[i]==p[0] or p[0]=='.'):
            if self.isMatch(s[i+1:],p):
                self.dic[(s,p)]=True
                return True
            i+=1
        self.dic[(s,p)]=self.isMatch(s,p[2:])
        return self.isMatch(s,p[2:])
