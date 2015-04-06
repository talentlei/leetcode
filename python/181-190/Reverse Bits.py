    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        strn=str(bin(n))
        strn=strn[2:]
        strn=list(strn)
        strn.reverse()
        res=''.join(strn)+(32-len(strn))*'0'
        return int(res,2)
