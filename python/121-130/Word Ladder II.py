class Solution:
    
    def getResult(self,visited,start,end):
    	# print start,end
        if end == start:
            return [[start]]
        res = []
        for w in visited[end]:
        	pre = self.getResult(visited,start,w)
        	res+=pre
        for line in res:
		    line.append(end)
        return res
            
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        res = []    
        if start == end:
            res.append([start])
            return res
	if start not in dict:
            dict.append(start)
        if end not in dict:
            dict.append(end)
        next = []
        visited = {}
        myMap = {}
        myMap[start]=1
        next.append(start)
        visited[start]=[-1]
        pos = 0
        while len(next)!=pos:
            word = next[pos]
            if end in myMap and myMap[word]>= myMap[end]:
                break
            for j in xrange(len(word)):
                for k in xrange(26):
                    nw = word[:j]+ chr(ord('a')+k) +word[j+1:]
                    if nw in dict and nw != word:
                        if nw not in myMap  :
                            myMap[nw] = myMap[word]+1
                            next.append(nw)
                            visited[nw]=[word]
                        elif  myMap[word] + 1== myMap[nw]:
                            visited[nw].append(word)
            pos+=1
        #get result
        if end not in myMap:
            return res
        # for k,v in visited.items():
        # 	print k,v
        res =self.getResult(visited, start,end)
        return res
