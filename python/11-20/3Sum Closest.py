class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        size = len(num)
        if size <3:
            return 2**32
        num.sort()
        i,mindiff,result =0,abs(num[0]+num[1]+num[2]-target),num[0]+num[1]+num[2]
        while i<size-2:
            twoSum = target-num[i]
            left,right = i+1,size-1
            while left <right:
                tempsum = num[left]+num[right]
                if tempsum==twoSum:
                    return target
                elif tempsum<twoSum:
                    left+=1
                else:
                    right-=1
                if abs(tempsum-twoSum) <mindiff:
                        mindiff = abs(tempsum-twoSum)
                        result = tempsum+num[i]
            ti=i
            while i<size-2 and num[ti]==num[i]:
                ti= i
                i+=1
        return result
