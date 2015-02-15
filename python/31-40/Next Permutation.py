class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        size = len(num)
        if size <2:
            return num
        i=size-2
        while i >=0:
            if num[i]<num[i+1]:
                pos = size-1
                while num[pos]<=num[i]:
                    pos-=1
                temp = num[i]
                num[i] = num[pos]
                num[pos]=temp
                break
            else:
                i-=1
        if i == -1:
            num.sort()
            return num
        return num[:i+1]+sorted(num[i+1:])
