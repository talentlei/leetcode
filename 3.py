class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        myMap={}
        start=0
        max=0
        for i in range(len(s)):
            if s[i] in myMap:
                for num in range(start,myMap[s[i]]):
                    myMap.pop(s[num])
                start=myMap[s[i]]+1
                myMap[s[i]]=i
            else:
                myMap[s[i]]=i
                if i-start+1>max:
                    max=i-start+1
        return max
