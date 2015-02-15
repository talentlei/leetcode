class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        size = len(s)
        if size <2:
            return 0
        stack = []
        Max,last = 0,-1
        for i in range(0,size):
            if s[i] =='(':
                stack.append(i)
            else:
                if len(stack)==0:
                    last = i
                else:
                    stack.pop()
                    if len(stack)==0:
                        Max = max(Max,i-last)
                    else:
                        Max = max(Max,i-stack[len(stack)-1])
        return Max
