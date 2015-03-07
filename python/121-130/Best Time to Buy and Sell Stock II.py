    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        profit = []
        for i in range(1,len(prices)):
            profit.append(prices[i]-prices[i-1])
        Max=0
        for i in range(len(profit)):
            if profit[i]>0:
                Max+=profit[i]
        return Max
