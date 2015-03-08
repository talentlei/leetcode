    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if len(num)<2:
            return len(num)
        Max=1
        Dict={}
        for data in num:
            if data not in Dict:
                left=Dict.get(data-1,0)
                right=Dict.get(data+1,0)
                res = left+right+1
                Max=max(Max,res)
                Dict[data]=res #important
                Dict[data-left]=res
                Dict[data+right]=res
        return Max
