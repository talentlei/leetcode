class Solution:
    # @param an integer
    # @return a list of string        
    def generateParenthesis(self, n):
        result = []
        if n == 0:
            result.append('')
            return result
        if n== 1:
            result.append('()')
            return result
        for i in range(0,n):
            for inner in self.generateParenthesis(i):
                for outer in self.generateParenthesis(n-i-1):
                    result.append('('+inner+')'+outer)
        return result
