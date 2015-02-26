 # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        ans=[]
        if not num:
            return ans
        num.sort()
        pos=0
        while pos<len(num):
            num[0],num[pos]=num[pos],num[0]
            myset=self.permute(num[1:])
            if myset:
                ans+=[[num[0]]+lis for lis in myset]
            else:
                ans+=[[num[0]]]
            num[0],num[pos]=num[pos],num[0]
            while pos+1 <len(num) and num[pos]==num[pos+1]:
                pos+=1
            pos+=1
        return ans
