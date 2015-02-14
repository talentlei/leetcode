class Solution:
    # @return a boolean
    def isValid(self, s):
        size = len(s)
        stack=[]
        for i in range(0,size):
            if s[i]=='(' or s[i] =='[' or s[i]=='{':
                stack.append(s[i])
            else:
                try:
                    if s[i]==')' and stack.pop()=='(':
                        continue
                    elif s[i]==']' and stack.pop()=='[':
                        continue
                    elif s[i]=='}' and stack.pop()=='{':
                        continue
                    else:
                        return False
                except:
                    return False
        return not stack
