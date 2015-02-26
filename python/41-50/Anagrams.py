class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        result=[]
        Dic={}
        for s in strs:
            l = list(s)
            l.sort()
            key = ''.join(l)
            if key in Dic:
                Dic[key].append(s)
            else:
                Dic[key]=[s]
        for key in Dic.keys():
            if len(Dic[key])>=2:
                result+=Dic[key]
        return result
