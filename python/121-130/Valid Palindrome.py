    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s==None or s=='':
            return True
        begin,end=0,len(s)-1
        while begin<end:
            while begin<end and not s[begin].isalnum():
                begin+=1
            while begin <end and not s[end].isalnum():
                end-=1
            if begin<end:
                if s[begin].lower()!=s[end].lower():
                    return False
            else:
                return True
            begin+=1
            end-=1
        return True
