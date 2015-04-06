def compare(x, y):
    return cmp((y+x),(x+y))
class Solution:
    def isZero(self,str):
        for i in str:
            if i!='0':
                return False
        return True
            
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if len(num)==0:
            return None
        tnum=[str(n) for n in num]
        tnum=sorted(tnum,cmp=compare)
        res=''.join(tnum)
        if self.isZero(res):
            return '0'
        return res
        
