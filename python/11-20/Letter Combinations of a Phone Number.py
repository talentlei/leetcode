class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        result,tempresult = [""],[]
        size = len(digits)
        maper = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for i in range(0,size):
            ch = digits[i]
            cand = maper[ch]
            for word in result:
                for c in cand:
                    tempresult.append(word+c)
            result = tempresult[:]
            tempresult=[]
        return result
