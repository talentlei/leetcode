    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        size = len(words)
        res = []
        if size==0:
            return res
        beg = 0
        while beg<size:
            cnt,wlen=0,0
            while beg+cnt <size and wlen+len(words[beg+cnt])<=maxWidth:
                wlen += len(words[beg+cnt])+1
                cnt += 1
            i = beg
            word = '' 
            if beg+cnt == size:
                while i<beg+cnt:
                    word +=  words[i]+' '
                    i+=1
                word = word.strip(' ')
                word += (maxWidth - len(word))*' '
                res.append(word)
            else:
                if cnt != 1:
                    dif = maxWidth -wlen+cnt
                    ss = dif/(cnt-1)
                    nt = cnt-1
                    while i <beg+cnt:
                        word += words[i]
                        if nt>0:
                            if dif%nt !=0:
                                word += ' '*(ss+1)
                                dif -= ss+1
                            elif dif%nt==0:
                                word += ' '*ss
                                dif -= ss
                            nt-=1
                        i+=1
                    word = word.strip(' ')
                else:
                    word = words[beg]
                    word += (maxWidth - len(word))*' '
                res.append(word)
            beg += cnt
        return res
