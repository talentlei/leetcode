    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings)==0:
            return 0
        candys=[]
        candys.append(1)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candys.append(candys[i-1]+1)
            else:
                candys.append(1)
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candys[i]=max(candys[i],candys[i+1]+1)
        return sum(candys)
