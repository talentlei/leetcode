    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result=0
        for data in A:
            result^=data
        return result
