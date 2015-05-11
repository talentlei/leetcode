class Solution:
            
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1 = list(num1)
        num2 = list(num2)
        res = ['0' for i in xrange(len(num1)+len(num2))]
        
        i=len(num1)-1
        while i>=0:
            add_in = 0
            j=len(num2)-1
            while j >=0:
                r = int(num1[i])*int(num2[j])+add_in+int(res[i+j+1])
                res[i+j+1] = str(r%10)
                add_in = r/10
                j-=1
            res[i]=str(add_in)
            i-=1
        pos = 0
        while pos <len(res) and res[pos]=='0':
            pos+=1
        if pos == len(res):
            return '0'
        return ''.join(res[pos:])
