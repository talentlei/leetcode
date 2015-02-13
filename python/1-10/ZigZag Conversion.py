class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        clc = nRows*2-2
        line = ''
        for i in range(nRows):
            if i == 0 or i == nRows-1:
                pos = i
                while pos<len(s):
                    line += s[pos]
                    pos += clc
            else:
                pos =i
                while pos<len(s):
                    line +=s[pos]
                    pos += clc-2*i
                    if pos < len(s):
                        line +=s[pos]
                        pos +=2*i
        return line
