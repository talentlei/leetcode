class Solution:
    def getNext(self,n):
        sum = 0
        nstr = str(n)
        for i in nstr:
            sum+=int(i)**2
        return sum
    # @param {integer} n
    # @return {boolean}
    record = []
    def isHappy(self, n):
        tmp = n
        self.record.append(tmp)
        while(tmp!=1):
             tmp = self.getNext(tmp)
             if tmp in self.record:
                 break
             self.record.append(tmp)
        return tmp==1
