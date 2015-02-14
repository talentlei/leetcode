class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    #can solve in O(n^2lgn) but not this method
    def fourSum(self, num, target):
        size = len(num)
        result = []
        num.sort()
        i,j =0,0
        while j <size-3:
            i = j+1
            while i<size-2:
                twoSum = target-num[i]-num[j]
                left,right = i+1,size-1
                while left <right:
                    if num[left]+num[right]==twoSum:
                        a = [num[j],num[i],num[left],num[right]]
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
            tj=j
            while j<size-3 and num[tj]==num[j]:
                tj= j
                j+=1
        return result
