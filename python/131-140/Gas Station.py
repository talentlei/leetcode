    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n= len(gas)
        begin,end=0,n
        while begin<n:
            end = begin+n
            temp=0
            index=begin
            while index<end:
                t=index%n
                temp +=gas[t]-cost[t]
                if temp<0:
                    break
                index+=1
            if index==end:
                return begin
            else :
                begin=index+1
        return -1
