    def convertToTitle(self, num):
        base=65
        result=''
        while num>0:
            num=num-1
            re = num%26
            result=chr(base+re)+result
            num=num/26
        return result
