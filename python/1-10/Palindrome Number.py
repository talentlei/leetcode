    # @return a boolean
    def isPalindrome(self, x):
        if x <0:
            return False
        temp,tempx=0,x
        while tempx!=0:
            temp = temp*10 + tempx%10
            tempx /=10
        return temp == x
