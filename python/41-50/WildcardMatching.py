def isMatch(self, s, p):
        star,ss = None,None
        size_s,size_p = len(s),len(p)
        ps,pp=0,0
        while ps < size_s:
            if pp<len(p) and (p[pp]=='?' or p[pp]==s[ps]):
                pp+=1
                ps+=1
                continue
            if pp<len(p) and p[pp]=='*':
                star = pp
                pp+=1
                ss = ps
                continue
            if star!=None:
                pp = star+1
                ps = ss+1
                ss+=1
                continue
            return False
        while pp < size_p and p[pp]=='*':
            pp+=1
        return pp==size_p
