    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones,twos=0,0
        for data in A:
            ones=(ones^data)&~twos
            twos=(twos^data)&~ones
        return ones
