class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        p = 0
        for e in A:
            if e != elem:
                A[p] = e
                p+=1
        return p
