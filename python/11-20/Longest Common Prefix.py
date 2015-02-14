class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        size = len(strs)
        if size==0:
            return ''
        strs.sort()
        lens = [len(i) for i in strs]
        minlen = min(lens)
        count=0
        for i in range(0,minlen):
            if strs[0][i]==strs[size-1][i]:
                count+=1
            else :
                break
        return strs[0][:count]
