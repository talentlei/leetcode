    # @return a boolean
    Dic={}
    def isScramble(self, s1, s2):
        key =s1+':'+s2
        if key in self.Dic:
            return self.Dic[key]
            
        n = len(s1)
        if n ==0 or s1==s2:
            self.Dic[key]=True
            return True
        for i in range(1,n):
            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]))  or\
             (self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i])):
                 self.Dic[key]=True
                 return True
        self.Dic[key]=False
        return False
