class Solution:
    # @return a string
    def intToRoman(self, num):
        if num <1 or num>3999:
            return ''
        maper = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        result =''
        step = 1000
        if num >0:
            pos,div = 0,0
            while step>0:
                if num>=step:
                    div = num/step
                    break
                step/=10
            if div == 4:
                result += maper[step]+maper[step*5]+self.intToRoman(num-div*step)
            elif div ==9:
                result += maper[step]+maper[step*10]+self.intToRoman(num-div*step)
            elif div>=5 and div <=8:
                result +=maper[step*5]+maper[step]*(div-5)+self.intToRoman(num-step*div)
            else:
                result += maper[step]*div+self.intToRoman(num-div*step)
        return result
