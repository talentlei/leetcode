#two sum
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic ={}
        counter=1
        for data in num:
            diff = target-data
            if diff in dic:
                return dic[diff],counter
            dic[data]=counter
            counter = counter+1
