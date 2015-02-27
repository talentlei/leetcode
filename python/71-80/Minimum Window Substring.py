    # @return a string
    def minWindow(self, S, T):
        if S=='' or T=='':
            return ''
        Dics={}
        temp={}
        for c in T:
            if  c in Dics:
                Dics[c]+=1
            else:
                Dics[c]=1
        counter,num=0,len(Dics)
        Min,result=len(S),''
        begin,end=0,0
        while end < len(S):
            ch = S[end]
            if ch in Dics:
                if ch in temp:
                    temp[ch]+=1
                else:
                    temp[ch]=1
                if temp[ch]==Dics[ch]:
                    counter+=1
                    
                if counter == num:
                    while counter==num:
                        if end-begin+1 <=Min:
                            Min = end-begin+1
                            result =S[begin:end+1]
                        c = S[begin]
                        begin+=1
                        if c in temp:
                            temp[c]-=1
                            if temp[c]<Dics[c]:
                                counter-=1
                        
            end+=1
        return result
