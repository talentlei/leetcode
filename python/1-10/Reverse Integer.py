class Solution:
    # @return an integer
    def reverse(self, x):
        isneg = False
        x = str(x)
        if x[0] == '-':
            isneg = True
            x = x[1:]
        x=x[::-1]
        if len(x)<10 or (len(x)==10 and x <'2147483647'):
            result = int(x)
            if isneg:
                result *=-1
            return result
        else :
            return 0
