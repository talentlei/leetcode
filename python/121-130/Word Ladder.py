    def ladderLength(self, beginWord, endWord, wordDict):
        if beginWord == endWord :
            return 1
        next = []
        visited = {}
        next.append(beginWord)
        visited[beginWord]=1
        pos = 0
        while len(next)!= pos:
            word = next[pos]
            for j in xrange(len(word)):
                for k in xrange(26):
                    nw = word[:j]+ chr(ord('a')+k) +word[j+1:]
                    if nw == endWord :
                        return visited[word]+1
                    if nw in wordDict and nw not in visited:
                        visited[nw] = visited[word]+1
                        next.append(nw)
            pos+=1
        return 0
