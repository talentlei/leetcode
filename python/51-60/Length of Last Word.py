    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        if not s:
            return 0
        words = s.split()
        return len(words[-1])
