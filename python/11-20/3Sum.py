class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        size = len(num)
        result = []
        num.sort()
        i =0
        while i<size-2:
            twoSum = -num[i]
            left,right = i+1,size-1
            while left <right:
                if num[left]+num[right]==twoSum:
                    a = [num[i],num[left],num[right]]
                    result.append(a)
                    tleft,tright = left,right
                    while left < right and num[tleft]==num[left]:
                        tleft= left
                        left+=1
                    while right > left and num[tright]==num[right]:
                        tright= right
                        right-=1
                elif num[left]+num[right]<twoSum:
                    left+=1
                else:
                    right-=1
            ti=i
            while i<size-2 and num[ti]==num[i]:
                ti= i
                i+=1
        return result
