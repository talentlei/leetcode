class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        size = len(num)
        if len(num)<2:
            return 0
            
        _min,_max=min(num),max(num)
        gap=int(math.ceil(float(_max-_min)/(size-1)))
        Maxbucket=[_min]*(size-1)
        Minbucket=[_max]*(size-1)
        for i in range(size):
            if num[i]==_min or num[i]==_max:
                continue
            
            bucketID=int((num[i]-_min)//gap)
            Maxbucket[bucketID]=max(Maxbucket[bucketID],num[i])
            Minbucket[bucketID]=min(Minbucket[bucketID],num[i])
        
        maxgap=gap
        pre=_min
        for i in range(size-1):
            if Maxbucket[i]==_min and Minbucket[i]==_max:
                continue
            maxgap=max(maxgap,Minbucket[i]-pre)
            pre = Maxbucket[i]
        maxgap=max(maxgap,_max-pre)
        return maxgap
            
