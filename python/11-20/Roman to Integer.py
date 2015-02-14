class Solution:
    # @return an integer
    def romanToInt(self, s):
        if s=='':
            return 0
        result = 0
        mapper = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
        for tp in mapper:
            pos = s.find(tp[1])
            if pos !=-1:
                return tp[0]-self.romanToInt(s[:pos])+self.romanToInt(s[pos+1:])
        return result
