    def isValid(self,loop,s):
        if loop==4 :
            if len(s)>0:
                return False,[]
            else:
                return True,[]
        result =[]
        for i in range(1,min(len(s),3)+1):
            ts = s[:i]
            if i>1 and ts[0]=='0':
                break
            if int(ts) <=255 :
                isOk,temp = self.isValid(loop+1,s[i:])
                if isOk:
                    if len(temp)==0:
                        result = [ts]
                    else:
                        result+= [ts+'.'+ip for ip in temp]
        if len(result)==0:
            return False,[]
        else:
            return True,result
            
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result=[]
        isOK,result = self.isValid(0,s)
        return result
