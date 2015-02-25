class Solution:
    # @return a string
    def countAndSay(self, n):
        times = 1
        rep = '1'
        while times!=n:
            Next=''
            rep+='#'
            count=1
            for i in range(1,len(rep)):
                if rep[i] == rep[i-1]:
                    count+=1
                else:
                    Next+=str(count)+rep[i-1]
                    count=1
            rep=Next
            times+=1
        return rep
