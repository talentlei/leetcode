    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            num = float(s)
        except:
            return False
        return True
