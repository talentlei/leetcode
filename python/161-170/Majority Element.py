    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate=num[0]
        time=1
        for i in range(1,len(num)):
            if time==0:
                candidate=num[i]
                time+=1
            else:
                if candidate==num[i]:
                    time+=1
                else:
                    time-=1
        return candidate
