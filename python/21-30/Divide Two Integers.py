class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor ==0 or (dividend==-2147483648 and divisor ==-1):
            return 2147483647
        if dividend ==0:
            return 0
        flag = 1
        if (dividend >0 and divisor <0) or (dividend <0 and divisor >0):
            flag = -1
        dividend,divisor=abs(long(dividend)),abs(long(divisor))
        if dividend <divisor:
            return 0
        result = 0
        rest = dividend
        while rest >= divisor:
            re = 1
            div = divisor
            rest -=divisor 
            while rest>= div:
                re +=re
                rest -= div
                div += div
            result+=re
        return flag*int(result)
