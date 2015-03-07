    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        profit = []
        for i in range(1,len(prices)):
            profit.append(prices[i]-prices[i-1])
        Max=profit[0]
        sum = 0
        for i in range(len(profit)):
            sum+=profit[i]
            if sum>Max:
                Max=sum
            if sum<0:
                sum=0
        
        return max(Max,0)
