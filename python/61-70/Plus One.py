    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        re =1
        for i in range(len(digits)-1,-1,-1):
            temp = re+digits[i]
            re = temp/10
            digits[i] = temp%10
            if re==0:
                break
        if re==1:
            digits.insert(0,1)
        return digits
