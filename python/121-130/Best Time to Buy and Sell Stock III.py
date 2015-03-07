    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        profit = []
        for i in range(1,len(prices)):
            profit.append(prices[i]-prices[i-1])
        pp,pr=[],[]
        Max=profit[0]
        sum=0
        for i in range(len(profit)):
            sum+=profit[i]
            if sum>Max:
                Max=sum
            if sum<0:
                sum=0
            pp.append(max(Max,0))
            
        Max=profit[len(profit)-1]
        sum=0
        for i in range(len(profit)-1,-1,-1):
            sum+=profit[i]
            if sum>Max:
                Max=sum
            if sum<0:
                sum=0
            pr.append(max(Max,0))
            
        Max = 0
        size=len(profit)
        for i in range(size-1):
            if pp[i]+pr[size-2-i]>Max:
                Max=pp[i]+pr[size-2-i]
        return max(Max,pp[size-1])
