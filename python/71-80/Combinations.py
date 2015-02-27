class Solution:
    result = []
    def subcombine(self,n,k,base,loop,pos,candi):
        if loop == k:
            self.result.append(candi)
            return
        for i in range(pos,n+1):
            if base[i-1]==0:
                base[i-1]=1
                candi.append(i)
                self.subcombine(n,k,base,loop+1,i+1,candi[:])
                base[i-1]=0
                candi.pop()
        return
    # @return a list of lists of integers
    def combine(self, n, k):
        base=[0 for i in range(0,n)]
        candi =[]
        loop,pos=0,1
        self.subcombine(n,k,base,loop,pos,candi)
        return self.result
