    def reverseWords(self, s):
        words=s.split()
        result=''
        if len(words)!=0:
            words.reverse()
            for word in words:
                result+=word+' '
        return result.rstrip()
